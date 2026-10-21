#!/usr/bin/env python3
"""Copy the public DS Labs pages into Firebase's isolated deploy directory.

The existing GitHub Pages site remains the source of truth.  Only these
explicitly listed PUBLIC files will ever enter firebase-site/.
"""
from pathlib import Path
from shutil import copy2

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "firebase-site"
FILES = (
    "index.html",
    "app-ads.txt",
    "privacy/scannexa/index.html",
    "privacy/arrowflow/index.html",
)

for relative in FILES:
    source = ROOT / relative
    destination = PUBLIC / relative
    if not source.is_file():
        raise SystemExit(f"Missing public source: {relative}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    copy2(source, destination)
    if source.read_bytes() != destination.read_bytes():
        raise SystemExit(f"Sync mismatch: {relative}")
    print(f"Synced {relative}")

publisher = (PUBLIC / "app-ads.txt").read_text(encoding="utf-8").strip()
expected = "google.com, pub-5743584111440579, DIRECT, f08c47fec0942fa0"
if publisher != expected:
    raise SystemExit("Unexpected AdMob seller record: review app-ads.txt before deployment")

print("Firebase public directory prepared; do not deploy files outside firebase-site/.")
