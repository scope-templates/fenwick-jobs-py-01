# Fenwick Jobs

Fenwick Jobs, batch jobs for a daily digest and image resizing. Two jobs, each a plain function with a
command-line entry point. Nothing in this repository schedules or queues them.

## Run locally

```sh
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m fenwick_jobs.digest               # digest for the latest day in data/items.json
python -m fenwick_jobs.digest 2026-10-03    # digest for one day
python -m fenwick_jobs.resize               # resizes data/images/*.png to 64x64 under out/
```

## Jobs

| Module           | Function                            | What it does                                                              |
| ---------------- | ----------------------------------- | ------------------------------------------------------------------------- |
| `jobs/digest.py` | `build_digest(date) -> dict`        | reads `data/items.json` for one day: total, count per category, top three by score |
| `jobs/resize.py` | `resize_batch(paths) -> list[Path]` | writes a 64x64 PNG per input image under `out/` and returns the written paths |

The `jobs/` directory is installed as the `fenwick_jobs` package (see `pyproject.toml`), so both modules run
with `python -m fenwick_jobs.<name>` after `pip install -e .`.

## Environment

| Variable   | Default  | Purpose                                   |
| ---------- | -------- | ----------------------------------------- |
| `DATA_DIR` | `./data` | where `items.json` and `images/` live     |
| `OUT_DIR`  | `./out`  | where resized images are written          |
