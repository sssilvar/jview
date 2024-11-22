"""Submodule for JSON structure definition inference."""

from typing import Any

TYPES_MAP = {
    str: "string",
    int: "number",
    float: "number",
    bool: "boolean",
    type(None): "null",
    list: "array",
    dict: "object",
}


def infer_type(value: Any) -> str:  # noqa: ANN401
    """Infer the type of a JSON value and return it as a string."""
    value_type = TYPES_MAP.get(type(value))
    if value_type:
        if isinstance(value, list) and len(value) == 0:
            return "empty array"
        return value_type
    return "unknown"


def infer_structure(data: dict[str, Any]) -> dict[str, Any]:
    """Infer JSON structure recursively, returning a dictionary."""
    if isinstance(data, dict):
        return {key: infer_structure(value) for key, value in data.items()}
    if isinstance(data, list):
        if len(data) == 0:
            return "empty array"
        return [infer_structure(data[0])]
    return infer_type(data)
