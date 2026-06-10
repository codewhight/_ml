import random
from nn0 import Value, Adam

# 設定隨機碼以利重現
random.seed(42)

# ==========================================
# 1. 生成二次曲線數據 (加上隨機噪聲)
# ==========================================
# 真實參數為 w2=2.0, w1=-3.0, b=1.0
true_w2, true_w1, true_b = 2.0, -3.0, 1.0
print(f"目標真實參數: w2={true_w2}, w1={true_w1}, b={true_b}")

X_data = []
y_data = []
for _ in range(50):
    x = random.uniform(-2.0, 2.0)
    noise = random.normalvariate(0, 0.2) # 均值為0，標準差為0.2的噪聲
    y = true_w2 * (x ** 2) + true_w1 * x + true_b + noise
    X_data.append(x)
    y_data.append(y)

# ==========================================
# 2. 定義模型參數與前向傳播
# ==========================================
# 隨機初始化模型參數 (w2, w1, b) 為 Value 物件
w2 = Value(random.uniform(-1.0, 1.0))
w1 = Value(random.uniform(-1.0, 1.0))
b = Value(random.uniform(-0.1, 0.1))

params = [w2, w1, b]

def forward(x):
    # y_pred = w2 * x^2 + w1 * x + b
    # x 是一個數字(float)，w2, w1, b 是 Value 物件
    # 由於 Value 與數字的運算，會將數字包裝成 Value
    return w2 * (x ** 2) + w1 * x + b

# ==========================================
# 3. 初始化優化器 (Adam)
# ==========================================
optimizer = Adam(params, lr=0.1)

# ==========================================
# 4. 訓練迴圈 (200 step)
# ==========================================
print("開始訓練二次多項式回歸模型...")
epochs = 200

for step in range(epochs):
    # 計算 MSE Loss
    step_loss = Value(0.0)
    for x, y in zip(X_data, y_data):
        pred = forward(x)
        error = pred - y
        # MSE 的項：error^2
        step_loss = step_loss + error ** 2
        
    loss = step_loss * (1.0 / len(X_data))
    
    # 反向傳播
    loss.backward()
    
    # 使用 Adam 更新權重
    optimizer.step()
    
    # 每 20 個 step 印出一次 loss
    if (step + 1) % 20 == 0:
        print(f"Step {step+1:3d}/{epochs}, Loss: {loss.data:.6f}")

# ==========================================
# 5. 驗證與結果比對
# ==========================================
print("\n訓練完成！參數結果比對：")
print(f"目標真實參數: w2={true_w2:.4f}, w1={true_w1:.4f}, b={true_b:.4f}")
print(f"模型學習參數: w2={w2.data:.4f}, w1={w1.data:.4f}, b={b.data:.4f}")
