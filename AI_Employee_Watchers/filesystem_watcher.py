# filesystem_watcher.py
# Bronze Tier - File drop watcher for Personal AI Employee

import time
from pathlib import Path
import shutil
import logging

# === CONFIG ===
VAULT_PATH = Path(r"D:\AI_Employee_Vault")          # ← yahan apna vault path daal do
INBOX_PATH = VAULT_PATH / "Inbox"
NEEDS_ACTION_PATH = VAULT_PATH / "Needs_Action"

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("FileWatcher")

def create_metadata_file(original_file: Path, copied_file: Path):
    """Copied file ke saath ek .md metadata file banata hai"""
    meta_path = copied_file.with_suffix(copied_file.suffix + '.md')
    content = f"""---
type: file_drop
original_name: {original_file.name}
size_bytes: {original_file.stat().st_size}
created: {time.strftime("%Y-%m-%d %H:%M:%S")}
---

New file dropped for processing.
Original location: {original_file}
"""
    meta_path.write_text(content, encoding="utf-8")
    logger.info(f"Metadata created: {meta_path}")

def process_new_file(file_path: Path):
    if not file_path.is_file():
        return

    dest_name = f"FILE_{file_path.name}"
    dest_path = NEEDS_ACTION_PATH / dest_name

    try:
        shutil.copy2(file_path, dest_path)
        logger.info(f"Copied: {file_path.name} → {dest_path}")
        create_metadata_file(file_path, dest_path)
    except Exception as e:
        logger.error(f"Error copying {file_path}: {e}")

def main():
    if not INBOX_PATH.exists():
        logger.warning(f"Creating Inbox folder: {INBOX_PATH}")
        INBOX_PATH.mkdir(parents=True, exist_ok=True)

    if not NEEDS_ACTION_PATH.exists():
        logger.warning(f"Needs_Action folder missing! Creating: {NEEDS_ACTION_PATH}")
        NEEDS_ACTION_PATH.mkdir(parents=True, exist_ok=True)

    logger.info("Starting File System Watcher...")
    logger.info(f"Watching: {INBOX_PATH}")

    processed = set()

    while True:
        try:
            for item in INBOX_PATH.iterdir():
                if item.is_file() and item.name not in processed:
                    process_new_file(item)
                    processed.add(item.name)
        except Exception as e:
            logger.error(f"Watcher error: {e}")

        time.sleep(10)  # har 10 second mein check

if __name__ == "__main__":
    main()