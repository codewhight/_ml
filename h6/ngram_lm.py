"""N‑gram 統計語言模型實作 (ngram_lm.py)

此檔案僅使用 Python 標準函式庫，不依賴任何第三方機器學習套件。
"""

from collections import Counter
from typing import List, Tuple

# ------------------------------------------------------------
# 1. Tokenization
# ------------------------------------------------------------

def tokenize(text: str) -> List[str]:
    """將輸入文字切分為 token 列表。
    - 中文：逐字切分（每個漢字視為一個 token）。
    - 英文/其他：以空白分詞。
    """
    if any('\u4e00' <= ch <= '\u9fff' for ch in text):
        # 中文模式：去除空白後逐字切分
        return [ch for ch in text if not ch.isspace()]
    else:
        # 英文或其他文字：以空白分割
        return text.split()

# ------------------------------------------------------------
# 2. 建立 N‑gram 計數
# ------------------------------------------------------------

def build_ngrams(tokens: List[str], n: int) -> Tuple[Counter, Counter]:
    """返回兩個 Counter：
    - ngram_counts: n‑gram 出現次數
    - prefix_counts: (n-1)-gram（作為條件前綴）出現次數
    """
    ngram_counts = Counter()
    prefix_counts = Counter()
    start_token = '<s>'
    padded = [start_token] * (n - 1) + tokens
    for i in range(len(padded) - n + 1):
        ngram = tuple(padded[i:i + n])
        prefix = ngram[:-1]
        ngram_counts[ngram] += 1
        prefix_counts[prefix] += 1
    return ngram_counts, prefix_counts

# ------------------------------------------------------------
# 3. N‑gram 語言模型類別
# ------------------------------------------------------------
class NGramLM:
    """簡易 N‑gram 語言模型（支援 bigram、trigram …）"""
    def __init__(self, n: int = 3):
        if n < 2:
            raise ValueError('n 必須 >= 2')
        self.n = n
        self.ngram_counts: Counter = Counter()
        self.prefix_counts: Counter = Counter()
        self.vocab: set = set()
        self.vocab_size: int = 0

    def fit(self, corpus: str):
        tokens = tokenize(corpus)
        self.vocab = set(tokens)
        self.vocab.add('<s>')  # 起始符號
        self.vocab_size = len(self.vocab)
        self.ngram_counts, self.prefix_counts = build_ngrams(tokens, self.n)

    def _conditional_prob(self, prefix: Tuple[str, ...], token: str) -> float:
        """返回 P(token | prefix) 使用 Laplace 平滑"""
        ngram = prefix + (token,)
        count_ngram = self.ngram_counts.get(ngram, 0)
        count_prefix = self.prefix_counts.get(prefix, 0)
        # (c+1) / (C + V)
        return (count_ngram + 1) / (count_prefix + self.vocab_size)

    def predict_next(self, context: List[str]) -> str:
        """根據最近 n-1 個 token，回傳機率最高的下一個 token"""
        if len(context) < self.n - 1:
            padded = ['<s>'] * (self.n - 1 - len(context)) + context
        else:
            padded = context[-(self.n - 1):]
        prefix = tuple(padded)
        best_token = None
        best_prob = -1.0
        for token in self.vocab:
            prob = self._conditional_prob(prefix, token)
            if prob > best_prob:
                best_prob = prob
                best_token = token
        return best_token

    def generate(self, prompt: str, max_len: int = 10) -> str:
        """從提示文字 `prompt` 產生最多 `max_len` 個 token（不含 prompt 本身）"""
        generated: List[str] = []
        context_tokens = tokenize(prompt)
        for _ in range(max_len):
            next_tok = self.predict_next(context_tokens + generated)
            if next_tok == '<s>':
                break
            generated.append(next_tok)
        # 合併回字串：中文逐字拼接，英文以空白連接
        if any('\u4e00' <= ch <= '\u9fff' for ch in prompt):
            return ''.join(generated)
        else:
            return ' '.join(generated)

# ------------------------------------------------------------
# 4. Demo / 測試
# ------------------------------------------------------------
if __name__ == '__main__':
    corpus = "今天天氣很好，我想出去玩。今天天氣很差，我只能待在家。"
    lm = NGramLM(n=3)  # Trigram
    lm.fit(corpus)
    prompt = "今天天氣"
    generated = lm.generate(prompt, max_len=10)
    print("Prompt :", prompt)
    print("Generated (10 tokens) :", generated)
