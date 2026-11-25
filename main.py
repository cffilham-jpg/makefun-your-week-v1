"""Write one UTF-8 week summary to the configured output directory.
The cat-review loss gives a hundred bounty attempts one compact, concrete twist.
"""

import os
from pathlib import Path


LINE = "Lost a hundred bounties to a cat review."

if not 1 <= len(LINE) <= 100:
    raise ValueError("The entry line must be between 1 and 100 characters.")

if not LINE.strip():
    raise ValueError("The entry line must not be empty or whitespace-only.")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))
