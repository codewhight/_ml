import random
from nn0 import Value, Adam, linear, softmax

# 設定隨機碼以利重現
random.seed(42)

# ==========================================
# 1. 準備模擬 Iris 數據集 (三分類，每類 3 個樣本)
# ==========================================
# 特徵維度: 4 (花萼長度, 花萼寬度, 花瓣長度, 花瓣寬度)
# 分類標籤: 0 (Setosa), 1 (Versicolor), 2 (Virginica)
X_data = [
    # Class 0
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [4.7, 3.2, 1.3, 0.2],
    # Class 1
    [7.0, 3.2, 4.7, 1.4],
    [6.4, 3.2, 4.5, 1.5],
    [6.9, 3.1, 4.9, 1.5],
    # Class 2
    [6.3, 3.3, 6.0, 2.5],
    [5.8, 2.7, 5.1, 1.9],
    [7.1, 3.0, 5.9, 2.1]
]
y_data = [0, 0, 0, 1, 1, 1, 2, 2, 2]

# ==========================================
# 2. 定義神經網路結構 (4 -> 8 -> 3)
# ==========================================
class MulticlassMLP:
    def __init__(self):
        # 隱藏層權重 (8 x 4) 與偏差 (8)
        self.w1 = [[Value(random.uniform(-0.5, 0.5)) for _ in range(4)] for _ in range(8)]
        self.b1 = [Value(random.uniform(-0.1, 0.1)) for _ in range(8)]
        
        # 輸出層權重 (3 x 8) 與偏差 (3)
        self.w2 = [[Value(random.uniform(-0.5, 0.5)) for _ in range(8)] for _ in range(3)]
        self.b2 = [Value(random.uniform(-0.1, 0.1)) for _ in range(3)]

    def __call__(self, x):
        # 隱藏層前向傳播: y1 = W1 @ x + b1
        h_logits = [y_i + b_i for y_i, b_i in zip(linear(x, self.w1), self.b1)]
        # 激勵函數 ReLU
        h = [val.relu() for val in h_logits]
        
        # 輸出層前向傳播: y2 = W2 @ h + b2
        logits = [y_o + b_o for y_o, b_o in zip(linear(h, self.w2), self.b2)]
        # 多分類 Softmax 函數
        probs = softmax(logits)
        return probs

    def parameters(self):
        # 收集所有參數量
        params = []
        for row in self.w1:
            params.extend(row)
        params.extend(self.b1)
        for row in self.w2:
            params.extend(row)
        params.extend(self.b2)
        return params

# ==========================================
# 3. 初始化模型與優化器 (Adam)
# ==========================================
model = MulticlassMLP()
optimizer = Adam(model.parameters(), lr=0.05)

# ==========================================
# 4. 訓練迴圈 (200 step)
# ==========================================
print("開始訓練鳶尾花三分類神經網路...")
epochs = 200

for step in range(epochs):
    step_loss = Value(0.0)
    for x, y in zip(X_data, y_data):
        probs = model(x)
        # 多分類交叉熵損失: -log(probs[target])
        eps = 1e-15
        loss_i = -(probs[y] + eps).log()
        step_loss = step_loss + loss_i
        
    loss = step_loss * (1.0 / len(X_data))
    
    # 反向傳播
    loss.backward()
    
    # 使用 Adam 優化器更新參數
    optimizer.step()
    
    # 每 20 個 step 印出一次 loss
    if (step + 1) % 20 == 0:
        print(f"Step {step+1:3d}/{epochs}, Loss: {loss.data:.6f}")

# ==========================================
# 5. 驗證與輸出預測結果
# ==========================================
print("\n訓練完成！開始驗證模擬鳶尾花分類：")
correct = 0
class_names = ["Setosa", "Versicolor", "Virginica"]

for i, (x, y) in enumerate(zip(X_data, y_data)):
    probs = model(x)
    prob_vals = [p.data for p in probs]
    pred_class = prob_vals.index(max(prob_vals))
    is_correct = (pred_class == y)
    if is_correct:
        correct += 1
    
    print(f"樣本 {i+1} 特徵: {x} -> 預測機率: [{', '.join(f'{p:.4f}' for p in prob_vals)}] | 預測: {class_names[pred_class]} (目標: {class_names[y]})")

accuracy = correct / len(X_data)
print(f"\n訓練集分類準確率: {accuracy * 100:.2f}% ({correct}/{len(X_data)})")
