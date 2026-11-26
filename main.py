import os
from pathlib import Path

TIP = "Tip: Restarting will not fix the bug, but it will give you 40 quiet seconds to remember you chose this career on purpose."


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TIP + "\n")


if __name__ == "__main__":
    main()
