"""Resize a batch of images to 64x64 PNG thumbnails under out/."""

import os
import sys
from collections.abc import Iterable
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = Path(os.environ.get("DATA_DIR", ROOT / "data"))
OUT_DIR = Path(os.environ.get("OUT_DIR", ROOT / "out"))
SIZE = (64, 64)


def resize_batch(paths: Iterable[Path | str], out_dir: Path = OUT_DIR) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for path in map(Path, paths):
        with Image.open(path) as image:
            thumbnail = ImageOps.fit(image.convert("RGBA"), SIZE)
        target = out_dir / f"{path.stem}_{SIZE[0]}x{SIZE[1]}.png"
        thumbnail.save(target, format="PNG")
        written.append(target)
    return written


def main(argv: list[str]) -> None:
    paths = [Path(arg) for arg in argv] or sorted((DATA_DIR / "images").glob("*.png"))
    for target in resize_batch(paths):
        print(target)


if __name__ == "__main__":
    main(sys.argv[1:])
