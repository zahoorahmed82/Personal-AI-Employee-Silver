# csv_drop_watcher.py - Silver Tier CSV/Invoices Drop Watcher
# Monitors DropBox folder for new CSV or PDF files

import time
import logging
from pathlib import Path
import shutil

# CONFIG
VAULT_PATH = Path(r"D:\Bronze Tier\AI_Employee_Vault")
DROP_BOX_PATH = VAULT_PATH / "DropBox"
NEEDS_ACTION = VAULT_PATH / "Needs_Action"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("CSVWatcher")

def process_new_file(file_path: Path):
    if not file_path.is_file():
        return

    # Sirf CSV ya PDF files process karo
    if file_path.suffix.lower() not in ['.csv', '.pdf']:
        logger.info(f"Ignored non-CSV/PDF file: {file_path.name}")
        return

    dest_name = f"DROP_{file_path.name}"
    dest_path = NEEDS_ACTION / dest_name

    try:
        shutil.copy2(file_path, dest_path)
        logger.info(f"Copied: {file_path.name} → {dest_path}")

        # Metadata file banao
        meta_path = dest_path.with_suffix(dest_path.suffix + '.md')
        content = f"""---
type: drop_file
original_name: {file_path.name}
size_bytes: {file_path.stat().st_size}
created: {time.strftime("%Y-%m-%d %H:%M:%S")}
priority: medium
---

New file dropped in DropBox for processing.
Type: {file_path.suffix.upper()}
Suggested Actions:
- [ ] Review CSV/PDF content
- [ ] Extract data (if CSV)
- [ ] Move to Done when complete
"""
        meta_path.write_text(content, encoding='utf-8')
        logger.info(f"Metadata created: {meta_path}")
    except Exception as e:
        logger.error(f"Error processing {file_path}: {e}")

def main():
    if not DROP_BOX_PATH.exists():
        logger.warning(f"Creating DropBox folder: {DROP_BOX_PATH}")
        DROP_BOX_PATH.mkdir(parents=True, exist_ok=True)

    logger.info(f"Starting CSV Drop Watcher... Watching: {DROP_BOX_PATH}")

    processed = set()

    while True:
        try:
            for item in DROP_BOX_PATH.iterdir():
                if item.is_file() and item.name not in processed:
                    process_new_file(item)
                    processed.add(item.name)
        except Exception as e:
            logger.error(f"Watcher error: {e}")

        time.sleep(10)  # har 10 second check

if __name__ == "__main__":
    main()