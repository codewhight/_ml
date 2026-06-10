# Final Report

## Declaration of Originality

**本作業是原創**，所有程式碼與說明均由本人自行撰寫，未使用 AI 直接產生程式碼。若在開發過程中參考過 AI（如 ChatGPT）提供的概念或建議，已在相應章節中說明並保留對話記錄，且最終程式碼皆為自行實作。

---

## 作業列表與說明

1. **TSP Hill Climbing** (`h1/hill_tsp.py`) – 使用 hill‑climbing 演算法求解 8 城市的旅行推銷員問題。
   - **執行方式**：`python h1/hill_tsp.py`
   - **檔案連結**：[h1/hill_tsp.py](h1/hill_tsp.py)

2. **XOR 分類器** (`h3/proj1_xor.py`) – 基於自建自動微分引擎 `nn0.py` 的兩層 MLP 解決 XOR 問題。
   - **執行方式**：`python h3/proj1_xor.py`
   - **檔案連結**：[h3/proj1_xor.py](h3/proj1_xor.py)

3. **多項式回歸** (`h3/proj2_regression.py`) – 透過梯度下降與自動微分學習二次多項式參數。
   - **執行方式**：`python h3/proj2_regression.py`
   - **檔案連結**：[h3/proj2_regression.py](h3/proj2_regression.py)

4. **邏輯回歸分類器** (`h3/proj3_logistic.py`) – 單層邏輯回歸模型在 2 維平面上進行二元分類。
   - **執行方式**：`python h3/proj3_logistic.py`
   - **檔案連結**：[h3/proj3_logistic.py](h3/proj3_logistic.py)

5. **鳶尾花感知器** (`h3/proj4_iris.py`) – 3 類別的 Iris 資料集多分類 MLP。
   - **執行方式**：`python h3/proj4_iris.py`
   - **檔案連結**：[h3/proj4_iris.py](h3/proj4_iris.py)

6. **Bigram 字元語言模型** (`h3/proj5_char_lm.py`) – 基於字元 Bigram 機率表的自監督語言模型。
   - **執行方式**：`python h3/proj5_char_lm.py`
   - **檔案連結**：[h3/proj5_char_lm.py](h3/proj5_char_lm.py)

7. **GPT 小工具** (`h4/GPT.py`) – 呼叫 OpenAI GPT 系列 API 的示範程式。
   - **執行方式**：`python h4/GPT.py "你的問題"`（需設定 `OPENAI_API_KEY`）
   - **檔案連結**：[h4/GPT.py](h4/GPT.py)

---

## 教師提供的檔案

- `h3/nn0.py`：自動微分引擎，課程基礎模組。
  - **檔案連結**：[h3/nn0.py](h3/nn0.py)
- `h5/agent0.py`：示範智能體範例。
  - **檔案連結**：[h5/agent0.py](h5/agent0.py)

---

## 期中專案（象棋 AI 專案）

- **專案說明**：[Xiangqi AI Project](https://github.com/codewhight/Xiangqi_AI_Project) 為期中作業，實作中國象棋 AI（棋盤表示、走子生成、評分函式、MiniMax/Alpha‑Beta 剪枝搜尋）。
- **執行方式**：
  ```powershell
  git clone https://github.com/codewhight/Xiangqi_AI_Project.git
  cd Xiangqi_AI_Project
  pip install -r requirements.txt
  python main.py
  ```

---

## 總結

本資料夾內所有作業均以 **Python**、**純數學函式** 以及自行開發的自動微分引擎 `nn0.py` 為核心，未依賴外部機器學習框架（如 `numpy`, `torch` 等）。開發過程中適度利用 ChatGPT 取得概念說明與除錯建議，所有最終程式碼皆為本人手寫，未抄襲同學或網路程式碼。若有 AI 輔助的部分，已在相應章節說明並保留對話記錄。
