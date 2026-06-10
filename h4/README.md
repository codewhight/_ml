# GPT.py Demo

This repository contains a minimal **mock GPT** implementation that demonstrates how to use a local text file as a data source for simple text generation. The purpose is educational – it shows how you could build a lightweight wrapper around a static corpus before integrating a real LLM API.

## Files
- **`tw.txt`** – The source corpus (Chinese sentences). Each line is a separate sentence that the mock model can return.
- **`GPT.py`** – The script that loads `tw.txt` and provides `SimpleGPT.generate(prompt)` which returns the most relevant line based on a naive keyword‑overlap scoring.
- **`README.md`** – This documentation (you are reading it!).

## How It Works
1. **Loading the data** – `SimpleGPT` reads all non‑empty lines from `tw.txt` into memory.
2. **Scoring** – For a given prompt, the `_score` method counts how many 2‑character substrings of the prompt appear in each line. This simple heuristic works reasonably well for Chinese text.
3. **Selection** – The line(s) with the highest score are collected and one is chosen at random. If every line scores `0`, a random line is returned.

## Usage
Run the script from the command line with a prompt:
```bash
python GPT.py "我看到一隻小貓"
```
The script prints a matching sentence from `tw.txt`.

### Example Output
```
我看到一隻小貓
```

## Extending the Demo
- Replace the scoring logic with a more sophisticated similarity measure (e.g., TF‑IDF, embeddings).
- Hook the `SimpleGPT.generate` method up to an actual LLM API (OpenAI, Anthropic, etc.) and use the output as a fallback.
- Add unit tests in a `tests/` directory to verify behavior.

## License
This demo is provided **as‑is** for educational purposes. Feel free to copy, modify, and redistribute.
