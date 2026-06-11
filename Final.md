# Final Report

## Declaration of Originality

**本作業是原創**，所有程式碼與說明均由本人自行撰寫。開發過程中若參考過 AI（如 AI）提供的概念或建議，已在相關章節說明並保留對話記錄，最終程式碼皆為自行實作，未複製任何同學或網路現成程式碼。

---

## 作業列表與說明

### 1. TSP Hill Climbing (`h1/hill_tsp.py`)
- **說明**：使用 Hill‑Climbing 局部搜尋演算法在 8 個預設城市座標上求解旅行推銷員問題（TSP），透過隨機交換兩座城市產生鄰近解，若距離更短則接受。最後繪製最佳路徑圖。
- **完成方式**：`python h1/hill_tsp.py`
- **說明文件**：[h1/README.md](h1/README.md)
- **AI 使用情形**：在實作 Hill‑Climbing 的迭代流程與程式注釋時向 Gemini 諮詢概念，對話連結：[AI 使用情形](https://gemini.google.com/share/8c259e3933a5)
- **抄襲聲明**：全部自行撰寫，未引用他人程式。

### 2. 題目圖檔 (`h2`)
- **說明**：本資料夾僅存放題目說明圖片，分別為 Q1、Q2。
- **連結**：
  - [Q1.jpg](h2/Q1.jpg)
  - [Q2.jpg](h2/Q2.jpg)
- **AI 使用情形**：無。
- **抄襲聲明**：圖片為課程提供，未自行創作，僅作為題目參考。

### 3. 基於自動微分引擎的機器學習專案 (`h3`)
以下每個子專案皆以自建的 `nn0.py` 為核心，自動微分與 Adam 優化，未使用外部 ML 框架。

#### 3.1 XOR 分類器 (`h3/proj1_xor.py`)
- **說明**：兩層 MLP 解決 XOR 非線性分類問題。使用自訂 Sigmoid 與 BCE 損失，Adam 更新參數。
- **完成方式**：`python h3/proj1_xor.py`
- **說明文件**：[h3/README.md](h3/README.md)
- **AI 使用情形**：在設定 Adam 超參數時向 AI 諮詢建議，對話已保留於 `h3/AI_chat.md`。
- **抄襲聲明**：全部自行實作。

#### 3.2 多項式回歸 (`h3/proj2_regression.py`)
- **說明**：透過梯度下降與自動微分學習二次多項式 $y = ax^2 + bx + c$ 的參數，最小化均方誤差 (MSE)。
- **完成方式**：`python h3/proj2_regression.py`
- **說明文件**：[h3/README.md](h3/README.md)
- **AI 使用情形**：撰寫 README 時參考 AI 的說明範例，已於 `h3/AI_chat.md` 記錄。
- **抄襲聲明**：自行實作。

#### 3.3 邏輯回歸分類器 (`h3/proj3_logistic.py`)
- **說明**：單層邏輯回歸模型在 2 維平面上執行二元分類，使用 BCE 損失與 Adam 優化。
- **完成方式**：`python h3/proj3_logistic.py`
- **說明文件**：[h3/README.md](h3/README.md)
- **AI 使用情形**：在 LaTeX 公式排版上向 AI 求助，已於 `h3/AI_chat.md` 保存對話。
- **抄襲聲明**：全部自行撰寫。

#### 3.4 鳶尾花感知器 (`h3/proj4_iris.py`)
- **說明**：多分類 MLP（4→8→3）使用 Softmax 與交叉熵損失，模擬 Iris 數據集的三類別分類。
- **完成方式**：`python h3/proj4_iris.py`
- **說明文件**：[h3/README.md](h3/README.md)
- **AI 使用情形**：無直接程式碼產出，由 AI 提供說明文字參考。
- **抄襲聲明**：自行實作。

#### 3.5 Bigram 字元語言模型 (`h3/proj5_char_lm.py`)
- **說明**：基於字元 Bigram 機率表的自監督語言模型，利用統計轉移矩陣生成文字。
- **完成方式**：`python h3/proj5_char_lm.py`
- **說明文件**：[h3/README.md](h3/README.md)
- **AI 使用情形**：在將 Bigram 機率轉為 Softmax 時向 AI 詢問實作細節，對話已於 `h3/AI_chat.md` 中保存。
- **抄襲聲明**：全部自行撰寫。

### 4. GPT Demo (`h4/GPT.py`)
- **說明**：示範呼叫 OpenAI GPT 系列 API 的簡易 wrapper，讀取本地語料 `tw.txt`，根據關鍵字相似度返回回應。
- **完成方式**：`python h4/GPT.py "你的問題"`（需設定環境變數 `OPENAI_API_KEY`）
- **說明文件**：[h4/README.md](h4/README.md)
- **AI 使用情形**：本身即為與 OpenAI 服務互動的程式，屬於「使用 AI」而非由 AI 產生程式碼。
- **抄襲聲明**：根據官方範例自行改寫。

### 5. 教師提供的檔案
- `h3/nn0.py`：自動微分引擎，課程基礎模組。  
  - **檔案連結**：[h3/nn0.py](h3/nn0.py)
- `h5/agent0.py`：示範智能體範例。  
  - **檔案連結**：[h5/agent0.py](h5/agent0.py)

### 6. 期中專案（象棋 AI）
- **說明**：實作中國象棋 AI，包含棋盤表示、走子生成、評分函式與 MiniMax/Alpha‑Beta 剪枝搜尋。  
- **執行方式**：
  ```powershell
  git clone https://github.com/codewhight/Xiangqi_AI_Project.git
  cd Xiangqi_AI_Project
  pip install -r requirements.txt
  python main.py
  ```
- **專案連結**：[Xiangqi AI Project](https://github.com/codewhight/Xiangqi_AI_Project)
- **AI 使用情形**：在開發過程中適度利用 AI 取得概念說明與除錯建議，相關對話已保存在各子目錄的 `AI_chat.md` 中。最終程式碼皆由本人手寫，未使用 AI 直接產生。
- **教師提供的檔案**：`h3/nn0.py` 與 `h5/agent0.py` 為課程提供的基礎模組，僅作為實驗基礎使用，未自行撰寫。

---

## 附錄：AI 與對話記錄

- 所有與 AI 互動的對話均保存在各子目錄的 `AI_chat.md` 中（例如 `h1/AI_chat.md`、`h3/AI_chat.md`、`h4/AI_chat.md`、`h5/AI_chat.md`、`h6/AI_chat.md`）。這些檔案紀錄了概念說明、除錯建議與程式細節的討論，屬於 **AI 輔助**，最終程式碼皆根據對話自行改寫。

---

## 總結

本資料夾內的所有作業均以 **Python**、**純數學函式** 與自行開發的自動微分引擎 `nn0.py` 為核心，未依賴外部機器學習框架（如 `numpy`、`torch` 等）。開發過程中適度利用 AI 取得概念說明與除錯建議，所有最終程式碼皆為本人手寫，未抄襲同學或網路程式碼。若有 AI 輔助的部分，已於相應章節說明並保留對話記錄。
