#!/usr/bin/env python3
"""Cutest picture entry: copy entry.png to the output directory.

Standard library only. No network access.
"""

import hashlib
import os
import shutil
import sys


def sha256_of(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)

    # Verify the output: it must exist and match the source byte for byte.
    if not os.path.isfile(dst):
        print(f"ERROR: output missing: {dst}", file=sys.stderr)
        return 1
    if os.path.getsize(dst) != os.path.getsize(src):
        print(
            f"ERROR: size mismatch: output {os.path.getsize(dst)} "
            f"!= source {os.path.getsize(src)}",
            file=sys.stderr,
        )
        return 1
    if sha256_of(dst) != sha256_of(src):
        print("ERROR: sha256 mismatch between output and source", file=sys.stderr)
        return 1
    print(f"Wrote {dst} ({os.path.getsize(dst)} bytes, verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
