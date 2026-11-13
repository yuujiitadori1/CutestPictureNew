# Cream Kitten Hugging a Chick

Entry for the make.fun "Make the cutest picture" bounty (cutest-picture-01).

## The picture

A cream kitten with blue eyes hugging a small chirping chick, wearing
a mint scarf. Soft pastel tones, gentle and warm — the cutest pair.

## Files

- `entry.png` — the picture (see facts below).
- `main.py` — copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
  (default `/output`). Standard library only, no network access, and it
  verifies the output exists and matches the source byte for byte
  (size + SHA-256) before exiting.
- `LICENSE` — MIT.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`.

## Image facts

- `entry.png`: 1024x1024, JPEG bytes (FF D8 magic), 149518 bytes.
  The file is named `entry.png` as required; the competition rules tell
  PNG and JPEG apart by first bytes, so JPEG bytes under the `.png`
  name are accepted.
- `main.py`: Python 3.13, standard library only, no network access.
