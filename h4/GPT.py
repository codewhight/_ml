'''GPT.py

A simple demonstration script that uses the contents of `tw.txt` as a mock data source.
It provides a very lightweight "text generation" interface that can be extended
to integrate with real LLM APIs.

Features
--------
- Load all lines from `tw.txt`.
- `SimpleGPT.generate(prompt: str) -> str` returns a line that best matches the
  prompt based on keyword overlap. If no match is found, a random line is
  returned.
- Command‑line interface for quick experimentation.

Usage
-----
```bash
python GPT.py "我看到一隻小貓"
```
The script will print a matching line from the data source.
''' 

import sys
import random
from pathlib import Path
from typing import List

DATA_FILE = Path(__file__).with_name('tw.txt')

class SimpleGPT:
    """A minimal mock GPT that selects lines from a data source.

    The class loads all lines from ``tw.txt`` (UTF‑8) and provides a ``generate``
    method that attempts to return the most relevant line for a given prompt.
    """

    def __init__(self, data_path: Path):
        if not data_path.is_file():
            raise FileNotFoundError(f"Data file not found: {data_path}")
        self.lines: List[str] = [line.strip() for line in data_path.read_text(encoding='utf-8').splitlines() if line.strip()]
        if not self.lines:
            raise ValueError("Data file is empty.")

    def _score(self, line: str, prompt: str) -> int:
        """Simple keyword overlap scoring.
        Returns the number of shared characters (or words) between the line and the prompt.
        """
        # For Chinese text we can count overlapping substrings of length 2
        # This is a naive heuristic but works for demonstration.
        score = 0
        for i in range(len(prompt) - 1):
            sub = prompt[i:i+2]
            if sub in line:
                score += 1
        return score

    def generate(self, prompt: str) -> str:
        """Return the line that best matches *prompt*.

        If multiple lines share the highest score, one of them is chosen at random.
        If every line scores ``0`` the result is a random line.
        """
        best_score = -1
        best_candidates: List[str] = []
        for line in self.lines:
            s = self._score(line, prompt)
            if s > best_score:
                best_score = s
                best_candidates = [line]
            elif s == best_score:
                best_candidates.append(line)
        return random.choice(best_candidates)


def main():
    if len(sys.argv) < 2:
        print("Usage: python GPT.py <prompt>")
        sys.exit(1)
    prompt = " ".join(sys.argv[1:])
    gpt = SimpleGPT(DATA_FILE)
    result = gpt.generate(prompt)
    print(result)

if __name__ == "__main__":
    main()
