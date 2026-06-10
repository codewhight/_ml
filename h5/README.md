# README.md - Secure Agent0

## Overview
`agent0.py` provides a simple command‑line interface for running machine‑learning related tasks (e.g., **train**, **evaluate**, **predict**).  The script is now fortified with **security controls** to mitigate common risks such as arbitrary code execution, path traversal, and uncontrolled resource consumption.

---

## Security Features
| Feature | Description |
|---------|-------------|
| **Argument Whitelisting** | Only tasks listed in `security_config.json → allowed_tasks` can be executed. |
| **Path Sanitisation** | User‑provided file paths are resolved and verified to stay inside the project’s `base_dir`. |
| **File‑size Limiting** | Files larger than `max_file_size_mb` (default 10 MB) are rejected. |
| **Robust Logging** | All actions, validations and errors are written to `logs/agent0.log` with a rotating file handler (1 MiB per file, keep 3 backups). |
| **Graceful Error Handling** | Exceptions are caught, logged and cause a clean exit with a non‑zero status code. |
| **Config‑driven Controls** | Security parameters are stored in `security_config.json`, allowing easy adjustments without touching code. |

---

## Configuration (`security_config.json`)
```json
{
    "allowed_tasks": ["train", "evaluate", "predict"],
    "base_dir": "path/to/your/project",  // automatically set to the script folder on first run
    "max_file_size_mb": 10
}
```
* **allowed_tasks** – Whitelist of task names the agent may run.
* **base_dir** – Root directory that all input files must reside in.  By default it is the directory containing `agent0.py`.
* **max_file_size_mb** – Upper bound for input file size.

---

## Usage
```bash
python agent0.py <task> <data_file>
```
* `<task>` – One of the whitelisted tasks (`train`, `evaluate`, `predict`).
* `<data_file>` – Path to the input data file (must be inside `base_dir` and smaller than the configured size).

### Examples
```bash
# Train a model using training data
python agent0.py train data/train.txt

# Evaluate the model
python agent0.py evaluate data/validation.txt

# Run predictions
python agent0.py predict data/test.txt
```
If an invalid task or an out‑of‑bounds path is supplied, the script will log an error and exit with status 1.

---

## Logging
All logs are stored under the `logs/` folder next to the script:
* `agent0.log` – Current log file (rotates after 1 MiB).
* `agent0.log.1`, `agent0.log.2`, `agent0.log.3` – Archived logs.

You can inspect the logs to audit what commands were executed and why a particular run failed.

---

## Extending the Agent
To add a new task:
1. Append the task name to `allowed_tasks` in `security_config.json`.
2. Implement the corresponding branch in `run_task` inside `agent0.py`.
3. Re‑run the script – the new task will be recognised automatically.

---

## License
This sample code is provided under the MIT License. Feel free to adapt it for your own projects while retaining the security pattern.
