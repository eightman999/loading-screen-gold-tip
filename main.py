import os
from pathlib import Path

TIP = "Tip: If the build fails three times, the fourth run is not a strategy. It is a ritual, and the compiler is not a god that accepts rituals."


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TIP + "\n")


if __name__ == "__main__":
    main()
