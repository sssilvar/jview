"""JViewer: A JSON data structure viewer.

Helps users understand JSON data structures by providing a visual representation
of the schema and relationships between fields.
"""

import argparse
import json
from pathlib import Path
from typing import Any, cast

from rich import print_json

from . import infer_structure


def parse_args() -> argparse.Namespace:
    """Parse arguments for the JViewer application."""
    parser = argparse.ArgumentParser(
        description="JViewer: A JSON data structure viewer.",
    )
    parser.add_argument("file", help="Path to the JSON file to view.")
    return parser.parse_args()


def _load_json(file_path: str | Path) -> dict[str, Any]:
    """Load JSON data from a file."""
    file_path = Path(file_path)
    with file_path.open() as file:
        return cast(dict[str, Any], json.load(file))


def main() -> None:
    """Run main entrypoint for parsing JSON data."""
    args = parse_args()
    data = _load_json(args.file)
    definition = infer_structure(data)

    print_json(json.dumps(definition, indent=2))


if __name__ == "__main__":
    main()
