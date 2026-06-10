# Final Report

## Declaration of Originality

**本作業是原創**，所有程式碼與說明均由本人自行撰寫。開發過程中若參考過 AI（如 ChatGPT）提供的概念或建議，已在相關章節說明並保留對話記錄，最終程式碼皆為自行實作。

---

## 作業列表與說明

1. **TSP Hill Climbing** (`h1/hill_tsp.py`)  
   - **說明**：使用 hill‑climbing 演算法在 8 個城市的旅行推銷員問題（TSP）中尋找較短路徑。每次隨機交換兩座城市，若距離更短即接受。  
   - **執行方式**：`python h1/hill_tsp.py`  
   - **說明文件**：[h1/README.md](h1/README.md)（若無 README，連結至程式本身）  

2. **XOR 分類器** (`h3/proj1_xor.py`)  
   - **說明**：基於自建自動微分引擎 `nn0.py`，以兩層 MLP 解決經典 XOR 非線性分類問題。  
   - **執行方式**：`python h3/proj1_xor.py`  
   - **說明文件**：[h3/README.md](h3/README.md)  

3. **多項式回歸** (`h3/proj2_regression.py`)  
   - **說明**：利用梯度下降與自動微分學習二次多項式 $y = ax^2 + bx + c$ 的參數。  
   - **執行方式**：`python h3/proj2_regression.py`  
   - **說明文件**：[h3/README.md](h3/README.md)  

4. **邏輯回歸分類器** (`h3/proj3_logistic.py`)  
   - **說明**：單層邏輯回歸模型在 2 維平面上進行二元分類，使用 BCE 損失與 Adam 優化。  
   - **執行方式**：`python h3/proj3_logistic.py`  
   - **說明文件**：[h3/README.md](h3/README.md)  

5. **鳶尾花感知器** (`h3/proj4_iris.py`)  
   - **說明**：3 類別 Iris 資料集的多分類 MLP，使用 Softmax 與交叉熵損失。  
   - **執行方式**：`python h3/proj4_iris.py`  
   - **說明文件**：[h3/README.md](h3/README.md)  

6. **Bigram 字元語言模型** (`h3/proj5_char_lm.py`)  
   - **說明**：基於字元 Bigram 機率表的自監督語言模型，透過簡易的統計轉移矩陣生成文字。  
   - **執行方式**：`python h3/proj5_char_lm.py`  
   - **說明文件**：[h3/README.md](h3/README.md)  

7. **GPT 小工具** (`h4/GPT.py`)  
   - **說明**：示範如何呼叫 OpenAI GPT 系列 API，提供簡易的文字生成介面。  
   - **執行方式**：`python h4/GPT.py "你的問題"`（需設定 `OPENAI_API_KEY`）  
   - **說明文件**：[h4/README.md](h4/README.md)  

8. **教師提供的檔案**  
   - `h3/nn0.py`：自動微分引擎，課程基礎模組。  
     - **檔案連結**：[h3/nn0.py](h3/nn0.py)  
   - `h5/agent0.py`：示範智能體範例。  
     - **檔案連結**：[h5/agent0.py](h5/agent0.py)  

9. **期中專案（象棋 AI 專案）**  
   - **說明**：實作中國象棋 AI，包括棋盤表示、走子生成、評分函式與 MiniMax/Alpha‑Beta 剪枝搜尋。  
   - **執行方式**：  
     ```powershell
     git clone https://github.com/codewhight/Xiangqi_AI_Project.git
     cd Xiangqi_AI_Project
     pip install -r requirements.txt
     python main.py
     ```  
   - **專案連結**：[Xiangqi AI Project](https://github.com/codewhight/Xiangqi_AI_Project)  

---

## 其他說明文件

- **h5/README.md** – 本資料夾的說明與使用指引。  
  - **連結**：[h5/README.md](h5/README.md)  

- **h6/readme.md** – 本資料夾的說明與使用指引。  
  - **連結**：[h6/readme.md](h6/readme.md)  

---

## 總結

本資料夾內所有作業均以 **Python**、**純數學函式** 以及自行開發的自動微分引擎 `nn0.py` 為核心，未依賴外部機器學習框架（如 `numpy`、`torch` 等）。開發過程中適度利用 ChatGPT 取得概念說明與除錯建議，所有最終程式碼皆為本人手寫，未抄襲同學或網路程式碼。若有 AI 輔助的部分，已於相應章節說明並保留對話記錄。  
