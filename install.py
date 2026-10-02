#!/usr/bin/env python3
"""Copy the bundled skill into a user-selected Codex skill directory."""
import argparse
from pathlib import Path
import shutil
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, default=Path.home() / ".agents" / "skills",
                        help="Parent skills directory (default: ~/.agents/skills)")
    args = parser.parse_args()
    source = Path(__file__).resolve().parent / "skills" / "psychology-skills"
    destination = args.dest.expanduser().resolve() / "psychology-skills"
    if not (source / "SKILL.md").is_file():
        parser.error("Incomplete download: skills/psychology-skills/SKILL.md is missing")
    if destination.exists() or destination.is_symlink():
        parser.error("Destination already exists; nothing changed: " + str(destination))
    # Reject copying the package into itself.
    if destination == source or source in destination.parents:
        parser.error("Destination must be outside the bundled skill")
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, destination)
    except OSError as error:
        print("Installation failed: " + str(error), file=sys.stderr)
        return 1
    print("Installed: " + str(destination))
    print("Start a new Codex turn and use $psychology-skills. Restart if it is not listed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
