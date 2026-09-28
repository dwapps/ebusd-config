#!/usr/bin/env python3
"""Mirror the published eBUS CSV tree and add the VR32 recoVAIR mapping."""

import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = ROOT / "upstream"
SITE = ROOT / "site"
LANGUAGES = ("de", "en", "next", "tt")
RECOVAIR_LANGUAGES = ("de", "en")
VR32_FILENAME = "38.v32.recov.csv"


def main() -> None:
    if not (UPSTREAM / "de" / "vaillant" / "08.recov.csv").is_file():
        raise SystemExit("Missing upstream eBUS CSV files")

    SITE.mkdir(exist_ok=True)
    for language in LANGUAGES:
        source = UPSTREAM / language
        target = SITE / language
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target, symlinks=False)

    for language in RECOVAIR_LANGUAGES:
        vaillant = SITE / language / "vaillant"
        shutil.copyfile(vaillant / "08.recov.csv", vaillant / VR32_FILENAME)

        index = vaillant / "index.json"
        names = json.loads(index.read_text(encoding="utf-8"))
        if not isinstance(names, str):
            raise SystemExit(f"Unexpected index format: {index}")
        files = names.splitlines()
        if VR32_FILENAME not in files:
            files.append(VR32_FILENAME)
        index.write_text(json.dumps("\n".join(sorted(files)), ensure_ascii=False), encoding="utf-8")

    (SITE / ".nojekyll").touch()


if __name__ == "__main__":
    main()

