# 基於 nn0.py 自動微分引擎的機器學習與深度學習實作專案

本目錄收錄了五個完全基於自訂自動微分引擎 [nn0.py](file:///c:/Users/user/Desktop/111210510/_ml/_ml/_ml/h3/nn0.py) 實作的獨立機器學習與深度學習專案。所有專案均不依賴 numpy, torch, scikit-learn 等第三方 ML 庫，僅使用純 Python 的 `math` 與隨機數模組，並統一使用 `nn0.py` 提供之 `Adam` 優化器進行訓練。

---

## 專案目錄與簡介

| 專案名稱 | 類型 | 數學核心 | 預期任務 |
| :--- | :--- | :--- | :--- |
| **[專案 1: XOR 分類器](file:///c:/Users/user/Desktop/111210510/_ml/_ml/_ml/h3/proj1_xor.py)** | 深度學習 (MLP) | 自訂 Sigmoid + BCE Loss | 解決經典 XOR 非線性分類問題 |
| **[專案 2: 多項式回歸](file:///c:/Users/user/Desktop/111210510/_ml/_ml/_ml/h3/proj2_regression.py)** | 機器學習 (回歸) | MSE Loss + 多項式擬合 | 擬合帶噪聲之二次曲線 $y = ax^2 + bx + c$ |
| **[專案 3: 邏輯回歸分類器](file:///c:/Users/user/Desktop/111210510/_ml/_ml/_ml/h3/proj3_logistic.py)** | 機器學習 (分類) | 自訂 Sigmoid + BCE Loss | 對二維線性可分數據群進行二元分類 |
| **[專案 4: 鳶尾花感知器](file:///c:/Users/user/Desktop/111210510/_ml/_ml/_ml/h3/proj4_iris.py)** | 深度學習 (多分類) | Softmax + 交叉熵 (Cross Entropy) | 對模擬 Iris 數據集進行 3 分類任務 |
| **[專案 5: Bigram 語言模型](file:///c:/Users/user/Desktop/111210510/_ml/_ml/_ml/h3/proj5_char_lm.py)** | 自然語言處理 (NLP) | `gd` 自監督學習 + 狀態轉移矩陣 | 字元級自回歸文本生成 (Autoregressive Generation) |

---

## 專案詳細說明

### 1. 專案一：自建 MLP 解決 XOR 問題 (`proj1_xor.py`)
* **這個專案在做什麼**：  
  解決經典的 XOR (互斥或) 邏輯閘分類問題。由於 XOR 是線性不可分的，必須透過具有至少一個隱藏層的神經網路 (MLP) 引入非線性特性來學習決策邊界。
* **數學與公式實作**：
  * **MLP 架構**：$2 \rightarrow 4 \rightarrow 1$。
  * **自訂 Sigmoid**：  
    $$\sigma(x) = \frac{1}{1 + e^{-x}}$$
    代碼實作為：`def sigmoid(x): return 1.0 / (1.0 + (-x).exp())`
  * **二元交叉熵損失 (BCE Loss)**：  
    $$\text{BCE} = - \frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(p_i) + (1 - y_i) \log(1 - p_i) \right]$$
* **運行方式**：
  ```powershell
  python proj1_xor.py
  ```
* **預期收斂 Loss**：$\approx 0.008$

---

### 2. 專案二：二次多項式回歸曲線擬合 (`proj2_regression.py`)
* **這個專案在做什麼**：  
  利用梯度下降與自動微分來尋找最適合的二次曲線參數。我們隨機生成了帶有高斯噪聲的二次曲線數據點，並訓練模型學回真正的參數。
* **數學與公式實作**：
  * **預測公式**：  
    $$\hat{y} = w_2 \cdot x^2 + w_1 \cdot x + b$$
  * **均方誤差 (MSE Loss)**：  
    $$\text{MSE} = \frac{1}{N} \sum_{i=1}^{N} (\hat{y}_i - y_i)^2$$
* **運行方式**：
  ```powershell
  python proj2_regression.py
  ```
* **預期結果**：模型學習出的參數 $w_2, w_1, b$ 會高度逼近真實設定的目標參數 $(2.0, -3.0, 1.0)$。

---

### 3. 專案三：邏輯回歸二元分類器 (`proj3_logistic.py`)
* **這個專案在做什麼**：  
  在二維空間中隨機生成兩個不同類別 (0 與 1) 的高斯分佈點群。本專案透過訓練一個單層邏輯回歸模型來找出劃分這兩群點的最優超平面（決策邊界）。
* **數學與公式實作**：
  * **模型前向傳播**：  
    $$z = w_1 x_1 + w_2 x_2 + b$$
    $$\hat{y} = \sigma(z)$$
  * 損失函數使用 BCE Loss。
* **運行方式**：
  ```powershell
  python proj3_logistic.py
  ```
* **預期結果**：訓練集分類準確率可達到 $100.00\%$，Loss 收斂至極低值 ($\approx 0.001$)。

---

### 4. 專案四：模擬鳶尾花多分類感知器 (`proj4_iris.py`)
* **這個專案在做什麼**：  
  擴展至**多分類問題 (Multiclass Classification)**。我們設計了一個簡化版且硬編碼的模擬 Iris (鳶尾花) 數據集，包含 3 個類別 (Setosa, Versicolor, Virginica)，每類有 4 維特徵。
* **數學與公式實作**：
  * **MLP 架構**：$4 \rightarrow 8 \rightarrow 3$。
  * **矩陣相乘**：呼叫 `nn0.py` 內建的 `linear(x, w)` 實作 $W \cdot x$。
  * **多分類 Softmax**：  
    $$\text{softmax}(z)_i = \frac{e^{z_i}}{\sum_{j} e^{z_j}}$$
  * **多分類交叉熵損失 (Cross-Entropy Loss)**：  
    $$\text{Loss} = - \frac{1}{N} \sum_{i=1}^{N} \log(p_{i, \text{target}})$$
* **運行方式**：
  ```powershell
  python proj4_iris.py
  ```
* **預期結果**：對 3 個類別的樣本輸出各自的機率向量（如 `[0.99, 0.00, 0.00]`），分類準確率為 $100.00\%$。

---

### 5. 專案五：自監督 Bigram 字元語言模型 (`proj5_char_lm.py`)
* **這個專案在做什麼**：  
  利用字元級 Bigram 頻率轉移機率進行自監督語言模型訓練。模型會讀取一段輸入文字 (例如 `"hello world!"`)，學習每個字元後面最可能出現的下一個字元，並利用學到的機率分佈自回歸生成文字。
* **數學與公式實作**：
  * **模型類別設計**：符合 `nn0.py` 內 `gd` 函數的規格，提供 `block_size`、`n_layer` 與 `__call__(token_id, pos_id, keys, values)`。
  * **損失與訓練**：呼叫 `nn0.py` 內建的 `gd(model, optimizer, tokens, step, num_steps)` 自動執行前向傳播、交叉熵計算、反向傳播與 Adam 更新。
  * **自回歸生成**：使用 Softmax 將 Logits 轉成機率，透過 `random.choices` 根據機率隨機抽樣下一個字元，並以此遞迴生成。
* **運行方式**：
  ```powershell
  python proj5_char_lm.py
  ```
* **預期結果**：
  模型能夠學會常見字元配對（例如：`h` 後面接 `e`，`w` 後面接 `o`），生成帶有類似原始訓練文本風格的字串（如 `"helo hrld! wo heorlo"`）。

---

## 如何執行驗證所有專案

您可以使用以下 powershell 指令逐一執行：

```powershell
# 執行專案 1
python proj1_xor.py

# 執行專案 2
python proj2_regression.py

# 執行專案 3
python proj3_logistic.py

# 執行專案 4
python proj4_iris.py

# 執行專案 5
python proj5_char_lm.py
```
