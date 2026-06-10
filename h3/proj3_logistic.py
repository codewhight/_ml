import random
from nn0 import Value, Adam

# 設定隨機碼以利重現
random.seed(42)

# ==========================================
# 1. 自訂 Sigmoid 函數與資料生成
# ==========================================
def sigmoid(x):
    return 1.0 / (1.0 + (-x).exp())

# 生成兩個類別的 2D 點群
# 類別 0: 中心在 (-1.5, -1.5)
# 類別 1: 中心在 (1.5, 1.5)
X_data = []
y_data = []

for _ in range(20):
    # 類別 0
    x1 = random.normalvariate(-1.5, 0.5)
    x2 = random.normalvariate(-1.5, 0.5)
    X_data.append([x1, x2])
    y_data.append(0.0)
    
    # 類別 1
    x1 = random.normalvariate(1.5, 0.5)
    x2 = random.normalvariate(1.5, 0.5)
    X_data.append([x1, x2])
    y_data.append(1.0)

# ==========================================
# 2. 初始化邏輯回歸權重與偏差
# ==========================================
# w1, w2, b 均包裝為 Value 物件
w1 = Value(random.uniform(-0.5, 0.5))
w2 = Value(random.uniform(-0.5, 0.5))
b = Value(0.0)

params = [w1, w2, b]

def predict(x):
    # z = w1 * x1 + w2 * x2 + b
    z = w1 * x[0] + w2 * x[1] + b
    return sigmoid(z)

# ==========================================
# 3. 初始化優化器 (Adam)
# ==========================================
optimizer = Adam(params, lr=0.1)

# ==========================================
# 4. 訓練邏輯回歸 (200 step)
# ==========================================
print("開始訓練邏輯回歸二元分類器...")
epochs = 200

for step in range(epochs):
    step_loss = Value(0.0)
    for x, y in zip(X_data, y_data):
        pred = predict(x)
        # BCE Loss
        eps = 1e-15
        loss_i = -(y * (pred + eps).log() + (1.0 - y) * (1.0 - pred + eps).log())
        step_loss = step_loss + loss_i
        
    loss = step_loss * (1.0 / len(X_data))
    
    # 反向傳播
    loss.backward()
    
    # 優化器更新
    optimizer.step()
    
    # 每 20 個 step 印出一次 loss
    if (step + 1) % 20 == 0:
        print(f"Step {step+1:3d}/{epochs}, Loss: {loss.data:.6f}")

# ==========================================
# 5. 驗證分類準確率 (Accuracy)
# ==========================================
correct = 0
for x, y in zip(X_data, y_data):
    pred = predict(x)
    pred_class = 1.0 if pred.data >= 0.5 else 0.0
    if pred_class == y:
        correct += 1

accuracy = correct / len(X_data)
print("\n訓練完成！驗證結果：")
print(f"決策邊界權重: w1={w1.data:.4f}, w2={w2.data:.4f}, b={b.data:.4f}")
print(f"訓練集分類準確率: {accuracy * 100:.2f}% ({correct}/{len(X_data)})")
