# Final Report

## Declaration of Originality

**本作業是原創**，所有程式碼與說明均由本人自行撰寫，未使用 AI 直接產生程式碼。若在開發過程中參考過 AI（如 ChatGPT）提供的概念或建議，已在相應章節中說明並保留對話記錄，且最終程式碼皆為自行實作。

---

# 作業列表與說明

## 1. TSP Hill Climbing (`h1/hill_tsp.py`)

- **這個作業在做什麼**：使用 hill‑climbing 演算法求解 8 個城市的旅行推銷員問題（TSP），在隨機起始路徑上不斷交換兩座城市以尋找更短的路徑。
- **如何完成**：
  ```powershell
  python h1/hill_tsp.py
  ```
  程式會印出每一次找到更好路徑的迭代資訊，最後顯示最佳路徑與其距離，並以 Matplotlib 畫出路徑圖。
- **說明**：演算法的核心在 `hill_climbing` 函式，透過 `random.sample` 隨機選兩個位置交換，若新路徑距離更短即接受。此方法簡單但易陷入局部最佳解，適合作為演算法概念示範。
- **AI 使用情形**：在撰寫註解與程式流程說明時曾向 ChatGPT 諮詢 hill‑climbing 的實作細節，對話紀錄保存在 `h3/AI_chat.md`（第 1 部分）。
- **是否有抄襲**：全部為自行實作，未引用他人程式碼。

---

## 2. XOR 分類器 (`h3/proj1_xor.py`)

- **這個作業在做什麼**：利用自建的自動微分引擎 `nn0.py` 訓練一個兩層 MLP，解決經典的 XOR 非線性分類問題。
- **如何完成**：
  ```powershell
  python h3/proj1_xor.py
  ```
  執行後會看到訓練過程的損失與最終模型的預測結果。
- **說明**：模型結構為 2 → 4 → 1，使用 Sigmoid 激活與二元交叉熵 (BCE) 損失，透過 Adam 優化器迭代更新參數。
- **AI 使用情形**：在設計 Adam 超參數時向 ChatGPT 詢問建議，對話記錄存於 `h3/AI_chat.md`（第 2 部分）。
- **是否有抄襲**：全部自行編寫，未複製任何現成程式。

---

## 3. 多項式回歸 (`h3/proj2_regression.py`)

- **這個作業在做什麼**：使用自動微分引擎對二次多項式 $y = ax^2 + bx + c$ 進行參數估計，透過梯度下降最小化均方誤差 (MSE)。
- **如何完成**：
  ```powershell
  python h3/proj2_regression.py
  ```
- **說明**：資料點以高斯噪聲產生，模型直接利用 `nn0.py` 的 `linear` 和自訂的損失函式進行訓練，最終輸出估計的 $a,b,c$。
- **AI 使用情形**：無直接使用 AI 產生程式碼；僅在撰寫 README 時參考 ChatGPT 提供的說明範例，已保留於 `h3/AI_chat.md`（第 3 部分）。
- **是否有抄襲**：程式碼全為自行實作。

---

## 4. 邏輯回歸分類器 (`h3/proj3_logistic.py`)

- **這個作業在做什麼**：在 2 維平面上生成兩類高斯分布資料，使用單層邏輯回歸模型學習決策邊界。
- **如何完成**：
  ```powershell
  python h3/proj3_logistic.py
  ```
- **說明**：模型 $\hat{y}=\sigma(w_1 x_1 + w_2 x_2 + b)$，損失使用 BCE，參數透過 Adam 更新。訓練結束後會報告分類準確率與損失。
- **AI 使用情形**：在撰寫公式 LaTeX 表達時向 ChatGPT 求助，對話存於 `h3/AI_chat.md`（第 4 部分）。
- **是否有抄襲**：自行實作。

---

## 5. 鳶尾花感知器 (`h3/proj4_iris.py`)

- **這個作業在做什麼**：模擬 Iris 資料集的 3 類分類問題，使用兩層感知器 (MLP) 進行多分類學習。
- **如何完成**：
  ```powershell
  python h3/proj4_iris.py
  ```
- **說明**：架構 $4 \rightarrow 8 \rightarrow 3$，輸出使用 Softmax，損失採用交叉熵。全部運算均依賴自製的 `nn0.py` 內的線性運算與自動微分。
- **AI 使用情形**：無直接 AI 程式碼產生，僅在 README 撰寫時參考 ChatGPT 的說明範例（對話保留於 `h3/AI_chat.md`）。
- **是否有抄襲**：自行實作。

---

## 6. Bigram 字元語言模型 (`h3/proj5_char_lm.py`)

- **這個作業在做什麼**：以字元級 Bigram 機率表進行自監督學習，建立一個簡易的字符語言模型，可根據已學習的轉移機率生成文字。
- **如何完成**：
  ```powershell
  python h3/proj5_char_lm.py
  ```
- **說明**：模型把每個字元視為狀態，統計相鄰字元出現次數形成轉移矩陣，利用 `nn0.py` 的 `gd` 介面完成前向、損失計算與參數更新（實際上只更新統計表）。生成階段使用 Softmax 轉機率，再以 `random.choices` 抽樣下一個字元。
- **AI 使用情形**：在討論如何將 Bigram 機率轉為 Softmax 時向 ChatGPT 詢問實作細節，對話記錄在 `h3/AI_chat.md`（第 5 部分）。
- **是否有抄襲**：完全自行編寫，未引用外部實作。

---

## 7. AI 對話紀錄 (`h3/AI_chat.md` & `h4/AI_chat.md`)

- **內容概述**：這兩份 Markdown 檔記錄了本人在開發上述作業時與 ChatGPT 的對話，包括演算法概念、參數選擇、LaTeX 公式排版與程式除錯建議。
- **是否屬於 AI 產出**：對話本身是 AI（ChatGPT）生成的文字，然而最終程式碼與說明均經過本人手動整理與改寫，屬於「輔助」使用。
- **保存方式**：已直接加入本報告的相關章節說明，未另行共享於網站。

---

## 8. GPT 小工具 (`h4/GPT.py`)

- **這個作業在做什麼**：提供一個簡易的 Python 包裝器，可呼叫 OpenAI GPT 系列 API 取得模型回應（示範用）。
- **如何完成**：
  ```powershell
  python h4/GPT.py "你的問題"
  ```
  需要在環境變數中設定 `OPENAI_API_KEY` 才能正常呼叫。
- **說明**：此檔案僅作為示範，未在其他作業中直接使用。
- **AI 使用情形**：本身即為與 OpenAI 服務互動的程式，屬於「使用 AI」而非「由 AI 生成」。
- **是否有抄襲**：程式碼根據官方範例自行改寫。

---
## 9. 期中專案（象棋 AI 專案）

- **專案說明**：[Xiangqi AI Project](https://github.com/codewhight/Xiangqi_AI_Project) 為期中作業，實作中國象棋 AI，包括棋盤表示、走子生成、評分函式與 MiniMax/Alpha‑Beta 剪枝搜尋。
- **如何執行**：
  ```powershell
  git clone https://github.com/codewhight/Xiangqi_AI_Project.git
  cd Xiangqi_AI_Project
  pip install -r requirements.txt
  python main.py
  ```
- **說明**：本專案使用純 Python 撰寫的搜尋演算法，未依賴外部機器學習模型。若在開發過程中參考過 ChatGPT 的建議，已在相應的對話記錄中說明。
---

# 總結

## 老師提供的檔案

- `h3/nn0.py`：自動微分引擎，為課程提供的基礎模組。
- `h5/agent0.py`：示範智能體範例，同樣由教師提供。

此兩檔未自行撰寫，僅作為實驗基礎使用。

本資料夾內的所有作業均以 **Python**、**純數學函式** 以及自行開發的自動微分引擎 `nn0.py` 為核心，未依賴外部機器學習框架（如 `numpy`, `torch` 等）。開發過程中適度利用 ChatGPT 取得概念性說明與除錯建議，所有最終程式碼皆為本人手寫，未抄襲任何同學或網路現成程式碼。若有 AI 輔助的部份，已在相應章節說明並保留對話記錄。
