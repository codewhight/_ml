# TSP Hill Climbing (`hill_tsp.py`)

## 任務說明

本作業實作 **旅行推銷員問題（TSP）** 的簡易求解器，使用 **Hill‑Climbing** 局部搜尋演算法在 8 個預設城市座標上尋找較短的巡迴路徑。每次隨機交換兩個城市的順序（產生鄰近解），若新路徑的總距離較目前解小則接受，重複迭代直至達到最大迭代次數或無更佳解為止。

## 檔案結構

- `hill_tsp.py` – 主程式，包含城市座標、距離計算、Hill‑Climbing 迴圈與繪圖展示。
- `requirements.txt` (若需要) – 只依賴 `matplotlib` 用於結果視覺化。

## 執行方式

```powershell
# 若尚未安裝 matplotlib，先執行
pip install matplotlib

# 執行 TSP 求解
python hill_tsp.py
```

執行後會在終端機印出每一次找到更好路徑的迭代資訊，最終顯示最佳路徑與總距離，並彈出 Matplotlib 視窗繪製路徑圖。

## 演算法說明

1. **初始化**：將 8 個城市座標隨機排列產生初始路徑。
2. **鄰域產生**：隨機抽取兩個位置交換，得到鄰近解。
3. **接受准則**：若鄰近解的總距離小於當前解，則接受該解。
4. **迭代上限**：預設 `max_iterations=1000`，可自行調整以觀察不同搜尋深度的效果。
5. **結果視覺化**：使用 Matplotlib 繪製城市與最佳路徑的折線圖。

## 參考資料

- Hill‑Climbing 為最簡單的局部搜尋方法，易於實作但容易停留在局部最佳解。
- 本範例的城市座標與程式碼皆為本人自行撰寫，未引用任何外部實作。
- 與gemini對話記錄:https://gemini.google.com/share/8c259e3933a5


---

*此 README 為本作業的說明文件，已在 `Final.md` 中以相對連結 `[h1/README.md](h1/README.md)` 提供。*
