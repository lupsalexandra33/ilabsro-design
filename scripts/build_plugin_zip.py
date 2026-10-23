#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import zipfile


ROOT = Path(__file__).resolve().parents[1]

PLUGIN_MANIFEST = ROOT / ".claude-plugin" / "plugin.json"

EXPECTED_PLUGIN_NAME = "ilabsro-design"
EXPECTED_PLUGIN_VERSION = "0.7.0"

RUNTIME_DIRECTORIES = [
    ".claude-plugin",
    "skills",
    "design-system",
    "assets",
    "generated-examples",
]

RUNTIME_ROOT_FILES = [
    "README.md",
]

RUNTIME_DOCS = [
    "USAGE.md",
    "EXAMPLES.md",
]

EXPECTED_TOP_LEVEL = {
    ".claude-plugin",
    "skills",
    "design-system",
    "assets",
    "generated-examples",
    "docs",
    "README.md",
}

IGNORED_NAMES = {
    "__pycache__",
    ".DS_Store",
    "Thumbs.db",
}

IGNORED_SUFFIXES = {
    ".pyc",
    ".pyo",
}

# Fixed ZIP timestamp makes repeated builds deterministic.
ZIP_TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build the ilabsro-design Claude runtime plugin ZIP."
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Destination path for the generated ZIP file.",
    )

    return parser.parse_args()


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def should_include(path: Path) -> bool:
    if path.name in IGNORED_NAMES:
        return False

    if path.suffix.lower() in IGNORED_SUFFIXES:
        return False

    if any(part in IGNORED_NAMES for part in path.parts):
        return False

    return True


def read_manifest() -> dict:
    if not PLUGIN_MANIFEST.is_file():
        fail(
            "missing plugin manifest: "
            ".claude-plugin/plugin.json"
        )

    try:
        data = json.loads(
            PLUGIN_MANIFEST.read_text(encoding="utf-8")
        )
    except Exception as exc:
        fail(f"could not read plugin manifest: {exc}")

    if data.get("name") != EXPECTED_PLUGIN_NAME:
        fail(
            "plugin manifest name must be "
            f"{EXPECTED_PLUGIN_NAME!r}"
        )

    if data.get("version") != EXPECTED_PLUGIN_VERSION:
        fail(
            "plugin manifest version must be "
            f"{EXPECTED_PLUGIN_VERSION}"
        )

    return data


def validate_sources() -> None:
    for relative in RUNTIME_DIRECTORIES:
        path = ROOT / relative

        if not path.is_dir():
            fail(f"missing runtime directory: {relative}")

    for relative in RUNTIME_ROOT_FILES:
        path = ROOT / relative

        if not path.is_file():
            fail(f"missing runtime file: {relative}")

    for filename in RUNTIME_DOCS:
        path = ROOT / "docs" / filename

        if not path.is_file():
            fail(f"missing runtime documentation: docs/{filename}")

    if not (ROOT / "skills" / "reels-maker" / "SKILL.md").is_file():
        fail("missing runtime skill: skills/reels-maker/SKILL.md")


def collect_files() -> list[tuple[Path, str]]:
    files: list[tuple[Path, str]] = []

    for directory in RUNTIME_DIRECTORIES:
        source_root = ROOT / directory

        for source in sorted(source_root.rglob("*")):
            if not source.is_file():
                continue

            if not should_include(source):
                continue

            archive_name = source.relative_to(ROOT).as_posix()
            files.append((source, archive_name))

    for relative in RUNTIME_ROOT_FILES:
        source = ROOT / relative
        files.append((source, relative))

    for filename in RUNTIME_DOCS:
        source = ROOT / "docs" / filename
        archive_name = f"docs/{filename}"
        files.append((source, archive_name))

    files.sort(key=lambda item: item[1])

    return files


def make_zip_info(archive_name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(
        filename=archive_name,
        date_time=ZIP_TIMESTAMP,
    )

    info.compress_type = zipfile.ZIP_DEFLATED

    # Regular file permissions: rw-r--r--
    info.external_attr = 0o100644 << 16

    return info


def build_zip(
    output: Path,
    files: list[tuple[Path, str]],
) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)

    if output.exists():
        output.unlink()

    with zipfile.ZipFile(
        output,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for source, archive_name in files:
            data = source.read_bytes()
            info = make_zip_info(archive_name)
            archive.writestr(info, data)


def verify_zip(output: Path) -> tuple[int, int, list[str]]:
    try:
        with zipfile.ZipFile(output, "r") as archive:
            names = archive.namelist()

            if not names:
                fail("generated ZIP is empty")

            file_names = [
                name for name in names
                if not name.endswith("/")
            ]

            top_level = sorted(
                {
                    name.split("/", 1)[0]
                    for name in file_names
                }
            )

            if set(top_level) != EXPECTED_TOP_LEVEL:
                fail(
                    "unexpected ZIP top-level entries: "
                    f"{top_level}"
                )

            if ".claude-plugin/plugin.json" not in file_names:
                fail(
                    ".claude-plugin/plugin.json is not directly "
                    "available at ZIP root"
                )

            if "docs/USAGE.md" not in file_names:
                fail("docs/USAGE.md missing from ZIP")

            if "docs/EXAMPLES.md" not in file_names:
                fail("docs/EXAMPLES.md missing from ZIP")

            forbidden_prefixes = (
                "artifact-index/",
                "showcase/",
                "scripts/",
                ".git/",
            )

            forbidden = [
                name
                for name in file_names
                if name.startswith(forbidden_prefixes)
            ]

            if forbidden:
                fail(
                    "forbidden runtime files found in ZIP: "
                    + ", ".join(forbidden[:10])
                )

            unexpected_docs = [
                name
                for name in file_names
                if name.startswith("docs/")
                and name
                not in {
                    "docs/USAGE.md",
                    "docs/EXAMPLES.md",
                }
            ]

            if unexpected_docs:
                fail(
                    "unexpected docs included in runtime ZIP: "
                    + ", ".join(unexpected_docs)
                )

            try:
                manifest = json.loads(
                    archive.read(
                        ".claude-plugin/plugin.json"
                    ).decode("utf-8")
                )
            except Exception as exc:
                fail(
                    "could not read plugin manifest from ZIP: "
                    f"{exc}"
                )

            if manifest.get("name") != EXPECTED_PLUGIN_NAME:
                fail(
                    "ZIP plugin name does not match expected value"
                )

            if manifest.get("version") != EXPECTED_PLUGIN_VERSION:
                fail(
                    "ZIP plugin version does not match "
                    f"{EXPECTED_PLUGIN_VERSION}"
                )

            bad_file = archive.testzip()

            if bad_file is not None:
                fail(f"ZIP integrity check failed at: {bad_file}")

            uncompressed_size = sum(
                info.file_size
                for info in archive.infolist()
                if not info.is_dir()
            )

            return (
                len(file_names),
                uncompressed_size,
                top_level,
            )

    except zipfile.BadZipFile as exc:
        fail(f"generated ZIP is invalid: {exc}")


def format_bytes(size: int) -> str:
    units = ["B", "KB", "MB", "GB"]
    value = float(size)

    for unit in units:
        if value < 1024 or unit == units[-1]:
            if unit == "B":
                return f"{int(value)} {unit}"
            return f"{value:.2f} {unit}"

        value /= 1024

    return f"{size} B"


def main() -> None:
    args = parse_args()

    manifest = read_manifest()
    validate_sources()

    files = collect_files()

    if not files:
        fail("no runtime files were collected")

    output = Path(args.output).expanduser().resolve()

    build_zip(output, files)

    file_count, uncompressed_size, top_level = verify_zip(
        output
    )

    zip_size = output.stat().st_size

    print(
        f"OK: built {manifest['name']} "
        f"v{manifest['version']}"
    )
    print(f"Output: {output}")
    print(f"Files: {file_count}")
    print(
        "Uncompressed source size: "
        f"{format_bytes(uncompressed_size)}"
    )
    print(f"ZIP size: {format_bytes(zip_size)}")
    print(
        "Top-level entries: "
        + ", ".join(top_level)
    )
    print(
        "Manifest at ZIP root: "
        ".claude-plugin/plugin.json"
    )


if __name__ == "__main__":
    main()
