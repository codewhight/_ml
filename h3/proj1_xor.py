import random
from nn0 import Value, Adam

# 設定隨機碼以利重現
random.seed(42)

# ==========================================
# 1. 自訂 Sigmoid 激勵函數
# ==========================================
def sigmoid(x):
    """使用 Value 節點的組合實作 Sigmoid：1 / (1 + e^-x)"""
    return 1.0 / (1.0 + (-x).exp())

# ==========================================
# 2. 定義神經元與多層感知器 (MLP)
# ==========================================
class Neuron:
    def __init__(self, nin):
        # 隨機初始化權重與偏差，並包裝成 Value 物件
        self.w = [Value(random.uniform(-0.8, 0.8)) for _ in range(nin)]
        self.b = Value(random.uniform(-0.1, 0.1))

    def __call__(self, x):
        # sum(wi * xi) + b
        act = sum((wi * xi) for wi, xi in zip(self.w, x)) + self.b
        return act

    def parameters(self):
        return self.w + [self.b]

class MLP:
    def __init__(self):
        # 建立 2 -> 4 -> 1 的網路結構
        # 隱藏層包含 4 個輸入為 2 的神經元
        self.hidden = [Neuron(2) for _ in range(4)]
        # 輸出層包含 1 個輸入為 4 的神經元
        self.output = Neuron(4)

    def __call__(self, x):
        # 隱藏層輸出並套用 Sigmoid 激勵函數
        h = [sigmoid(n(x)) for n in self.hidden]
        # 輸出層輸出並套用 Sigmoid 轉換為機率
        out = sigmoid(self.output(h))
        return out

    def parameters(self):
        # 收集所有網路權重與偏差
        params = []
        for n in self.hidden:
            params.extend(n.parameters())
        params.extend(self.output.parameters())
        return params

# ==========================================
# 3. 準備 XOR 資料集
# ==========================================
X = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
y = [0.0, 1.0, 1.0, 0.0]

# ==========================================
# 4. 初始化模型與優化器
# ==========================================
model = MLP()
optimizer = Adam(model.parameters(), lr=0.1)

# ==========================================
# 5. 訓練迴圈 (200 step)
# ==========================================
print("開始訓練 XOR 分類神經網路...")
epochs = 200

for step in range(epochs):
    # 前向傳播與計算 BCE Loss
    step_loss = Value(0.0)
    for xi, yi in zip(X, y):
        pred = model(xi)
        # 實作 BCE Loss: - (y * log(p) + (1 - y) * log(1 - p))，加上極小值防止 log(0)
        eps = 1e-15
        loss_i = -(yi * (pred + eps).log() + (1.0 - yi) * (1.0 - pred + eps).log())
        step_loss = step_loss + loss_i
    
    # 計算平均 Loss
    loss = step_loss * (1.0 / len(X))
    
    # 反向傳播
    loss.backward()
    
    # 使用 Adam 更新權重
    optimizer.step()
    
    # 每 20 個 step 印出一次 loss
    if (step + 1) % 20 == 0:
        print(f"Step {step+1:3d}/{epochs}, Loss: {loss.data:.6f}")

# ==========================================
# 6. 驗證與預測結果
# ==========================================
print("\n訓練完成！開始驗證 XOR 模型：")
for xi, yi in zip(X, y):
    pred = model(xi)
    print(f"輸入: {xi} -> 預測機率: {pred.data:.4f} (目標標籤: {yi:.1f})")
