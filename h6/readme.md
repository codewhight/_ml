# N‑gram 統計語言模型說明文件

## 目標
- 依據給定的文字序列，預測下一個最可能出現的字或詞。
- 完全不使用 Transformer、Attention 或任何自注意力機制，符合題目嚴格限制。

## 主要流程概述
1. **Tokenization**：
   - 中文：逐字切分（每個漢字視為一個 token）。
   - 英文或其他語言：以空白分詞。
2. **建立 N‑gram 計數**：
   - 統計所有 n‑gram（預設 n=3）與 (n‑1)-gram 的出現次數。
   - 為了支援句首預測，前面補上 `<s>` 標記作為起始符號。
3. **平滑 (Laplace / Add‑1)**：
   - 防止 zero‑probability，對每個條件機率加 1，除以 `前綴次數 + 詞表大小`。
4. **預測與生成**：
   - `predict_next(context)`：根據最近 n‑1 個 token，計算每個候選 token 的條件機率，回傳機率最高者。
   - `generate(prompt, max_len=10)`：從提示文字 `prompt` 出發，迭代呼叫 `predict_next` 最多生成 `max_len` 個 token（不含 prompt 本身）。

## 方法說明與為何不使用 Attention
- **統計模型**：模型僅透過簡單的查表（dictionary）操作取得條件機率，沒有向量運算、矩陣乘法或注意力權重計算。
- **固定上下文窗口**：預測僅依賴最近 `n‑1` 個 token，沒有全局依賴或動態加權，徹底避免任何形式的 self‑attention。

## 長文本上的局限性
1. **資料稀疏**：隨著 n 增大，可能的 n‑gram 組合呈指數增長，許多組合在語料中未出現，導致機率估計不準確。即使使用 Laplace 平滑，仍會產生過度平滑的問題。
2. **固定上下文窗口**：模型只能看到最近 `n‑1` 個 token，無法捕捉遠距離依賴（如長句子、篇章結構）。
3. **無語意表示**：不像詞向量或神經網路能學到語意相似度，統計模型只能靠共現頻率，對同義詞、變形詞的泛化能力極差。
4. **生成品質**：在長文本生成時，容易出現重複或死循環，尤其當語料較小時更明顯。

## 使用方式
1. 下載/複製 `ngram_lm.py` 到同一目錄（`C:\Users\user\Desktop\111210510\_ml\_ml\_ml\h6`）。
2. 在命令列執行：
   ```bash
   python ngram_lm.py
   ```
   會看到示範文本的預測結果。
3. 如需自行訓練或生成，只需在 Python 程式中匯入 `NGramLM` 類別：
   ```python
   from ngram_lm import NGramLM
   lm = NGramLM(n=3)
   lm.fit(your_corpus)
   result = lm.generate(prompt="今天天氣", max_len=10)
   print(result)
   ```

## 範例說明（已在程式中提供）
- **語料**：`"今天天氣很好，我想出去玩。今天天氣很差，我只能待在家。"`
- **模型**：使用 Trigram（n=3）訓練。
- **生成**：以提示 `"今天天氣"` 為起點，產生最長 10 個字的後續文字。
- **輸出**：在執行 `python ngram_lm.py` 時會印出 `Prompt` 與 `Generated (10 tokens)` 的結果。

---

如需調整 n‑gram 的大小、平滑方式或生成長度，只需修改 `ngram_lm.py` 中對應的參數即可。
