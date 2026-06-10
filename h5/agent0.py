# agent0.py - Secure Agent with Safety Controls
"""
Secure Agent Implementation

Features:
- Argument parsing with strict validation
- Whitelisted task execution to prevent arbitrary code execution
- Input file path sanitization (ensures paths stay within the project directory)
- Comprehensive logging with rotating file handler
- Exception handling with clear error messages
- Configuration driven whitelist (JSON file `security_config.json`)
"""

import argparse
import json
import logging
import os
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler

# ---------- Logging Setup ----------
LOG_DIR = Path(__file__).resolve().parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
logger = logging.getLogger("agent0")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(LOG_DIR / "agent0.log", maxBytes=1_048_576, backupCount=3)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# ---------- Security Configuration ----------
CONFIG_PATH = Path(__file__).resolve().parent / "security_config.json"

DEFAULT_CONFIG = {
    "allowed_tasks": ["train", "evaluate", "predict"],
    "base_dir": str(Path(__file__).resolve().parent),
    "max_file_size_mb": 10
}

if CONFIG_PATH.is_file():
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            CONFIG = json.load(f)
    except Exception as e:
        logger.error(f"Failed to load security_config.json: {e}")
        CONFIG = DEFAULT_CONFIG
else:
    CONFIG = DEFAULT_CONFIG
    # Write default config for future reference
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(DEFAULT_CONFIG, f, indent=4)
        logger.info("Created default security_config.json")

BASE_DIR = Path(CONFIG.get("base_dir", ".")).resolve()
ALLOWED_TASKS = set(CONFIG.get("allowed_tasks", []))
MAX_FILE_SIZE = CONFIG.get("max_file_size_mb", 10) * 1024 * 1024

# ---------- Helper Functions ----------
def safe_path(path_str: str) -> Path:
    """Resolve a user‑provided path and ensure it stays within BASE_DIR."""
    p = Path(path_str).expanduser().resolve()
    if BASE_DIR not in p.parents and p != BASE_DIR:
        raise ValueError(f"Path '{p}' is outside the allowed directory '{BASE_DIR}'.")
    return p

def validate_file(path: Path) -> None:
    """Check file existence and size limits."""
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")
    size = path.stat().st_size
    if size > MAX_FILE_SIZE:
        raise ValueError(f"File {path} exceeds size limit of {MAX_FILE_SIZE / (1024*1024)} MB.")

def run_task(task: str, data_path: str) -> None:
    """Execute a whitelisted task safely.

    Args:
        task: Name of the task (must be in ALLOWED_TASKS).
        data_path: Path to the input data file.
    """
    if task not in ALLOWED_TASKS:
        raise PermissionError(f"Task '{task}' is not permitted. Allowed: {sorted(ALLOWED_TASKS)}")
    try:
        data_file = safe_path(data_path)
        validate_file(data_file)
    except Exception as e:
        logger.error(f"Data validation failed: {e}")
        raise

    # Placeholder for actual task implementation – keep it sandboxed.
    logger.info(f"Executing task '{task}' on data file '{data_file}'.")
    # Example stub actions
    if task == "train":
        logger.info("Training model... (stub)")
    elif task == "evaluate":
        logger.info("Evaluating model... (stub)")
    elif task == "predict":
        logger.info("Running predictions... (stub)")
    else:
        # Should never reach here due to whitelist check
        logger.warning(f"Unhandled task '{task}'.")

# ---------- Main Entry Point ----------
def parse_args():
    parser = argparse.ArgumentParser(description="Secure Agent0 CLI")
    parser.add_argument("task", type=str, help="Task to execute (whitelisted).")
    parser.add_argument("data", type=str, help="Path to input data file.")
    return parser.parse_args()

def main():
    try:
        args = parse_args()
        run_task(args.task, args.data)
    except Exception as exc:
        logger.exception(f"Agent terminated with error: {exc}")
        sys.exit(1)

if __name__ == "__main__":
    main()
