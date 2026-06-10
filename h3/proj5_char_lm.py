import random
import math
from nn0 import Value, Adam, gd

# 設定隨機碼以利重現
random.seed(42)

# ==========================================
# 1. 準備訓練文本與 Tokenizer
# ==========================================
text = "hello world! hello world! hello world!"
vocab = sorted(list(set(text)))
vocab_size = len(vocab)
print(f"訓練文本: '{text}'")
print(f"詞彙表大小: {vocab_size}, 包含: {vocab}")

char_to_id = {c: i for i, c in enumerate(vocab)}
id_to_char = {i: c for i, c in enumerate(vocab)}
tokens = [char_to_id[c] for c in text]

# ==========================================
# 2. 定義符合 gd 接口的 Bigram 語言模型
# ==========================================
class BigramLanguageModel:
    def __init__(self, vocab_size):
        # 為了滿足 gd 函數的接口要求
        self.block_size = len(tokens) - 1 # 設定足夠大的區塊以處理整條序列
        self.n_layer = 1                  # 虛擬層數，用於初始化 keys/values
        
        # 狀態轉移矩陣 (vocab_size x vocab_size)
        # 代表輸入字元預測下一個字元的權重
        self.w = [[Value(random.uniform(-0.1, 0.1)) for _ in range(vocab_size)] for _ in range(vocab_size)]

    def __call__(self, token_id, pos_id, keys, values):
        # 輸入當前的字元 ID，返回對下一個字元的預測 logits (大小為 vocab_size 的 Value 列表)
        return self.w[token_id]

    def parameters(self):
        # 收集所有的權重參數
        params = []
        for row in self.w:
            params.extend(row)
        return params

# ==========================================
# 3. 初始化模型與優化器 (Adam)
# ==========================================
model = BigramLanguageModel(vocab_size)
optimizer = Adam(model.parameters(), lr=0.1)

# ==========================================
# 4. 呼叫 nn0.py 的 gd 函數進行訓練 (200 step)
# ==========================================
print("開始訓練 Bigram 語言模型...")
epochs = 200

for step in range(epochs):
    # gd 函數內部會執行 forward -> loss -> backward -> Adam update -> 清空梯度
    loss_data = gd(model, optimizer, tokens, step, epochs)
    
    # 每 20 個 step 印出一次 loss
    if (step + 1) % 20 == 0:
        print(f"Step {step+1:3d}/{epochs}, Loss: {loss_data:.6f}")

# ==========================================
# 5. 驗證：進行自回歸文本生成 (Autoregressive Generation)
# ==========================================
def generate_text(model, start_char, length=20):
    current_char = start_char
    generated = [current_char]
    
    # 建立虛擬 keys 與 values 供 __call__ 參數使用
    keys = [[] for _ in range(model.n_layer)]
    values = [[] for _ in range(model.n_layer)]
    
    for _ in range(length):
        token_id = char_to_id[current_char]
        # 獲取模型 logits
        logits = model(token_id, 0, keys, values)
        
        # 利用數學公式計算 softmax 概率值 (進行採樣)
        max_val = max(v.data for v in logits)
        exps = [math.exp(v.data - max_val) for v in logits]
        total_sum = sum(exps)
        probs = [e / total_sum for e in exps]
        
        # 根據學習到的機率分佈採樣下一個字元
        next_id = random.choices(range(vocab_size), weights=probs)[0]
        current_char = id_to_char[next_id]
        generated.append(current_char)
        
    return "".join(generated)

print("\n訓練完成！自回歸文字生成測試：")
# 分別以不同的起手字生成文字
for start in ['h', 'w', 'l']:
    gen = generate_text(model, start, length=25)
    print(f"以 '{start}' 開頭生成: '{gen}'")
