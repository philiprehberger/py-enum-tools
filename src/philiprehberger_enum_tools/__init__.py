"""Practical utilities for Python enums — lookup, validation, listing, and serialization."""

from __future__ import annotations

import enum
import json
from enum import Enum
from typing import Any

__all__ = [
    "lookup",
    "choices",
    "values",
    "names",
    "validate",
    "AutoEnum",
    "SerializableEnum",
    "SerializableEncoder",
]


def lookup(enum_class: type[Enum], value: Any, *, default: Any = None) -> Enum | None:
    """Safe value-to-member lookup. Returns default if not found."""
    for member in enum_class:
        if member.value == value:
            return member
    return default


def choices(enum_class: type[Enum]) -> list[tuple[Any, str]]:
    """Return a list of (value, name) tuples, useful for forms and CLIs."""
    return [(member.value, member.name) for member in enum_class]


def values(enum_class: type[Enum]) -> list[Any]:
    """Return a list of all member values."""
    return [member.value for member in enum_class]


def names(enum_class: type[Enum]) -> list[str]:
    """Return a list of all member names."""
    return [member.name for member in enum_class]


def validate(enum_class: type[Enum], value: Any) -> Enum:
    """Lookup a value and return the member, or raise ValueError with valid options."""
    result = lookup(enum_class, value)
    if result is not None:
        return result
    valid = ", ".join(repr(v) for v in values(enum_class))
    raise ValueError(
        f"{value!r} is not a valid {enum_class.__name__} value. "
        f"Valid values: {valid}"
    )


class AutoEnum(Enum):
    """Enum subclass where auto() generates lowercase member name as value."""

    @staticmethod
    def _generate_next_value_(
        name: str, start: int, count: int, last_values: list[Any]
    ) -> str:
        return name.lower()


class SerializableEnum(Enum):
    """Enum that serializes to its value in JSON."""

    def __json__(self) -> Any:
        """Return the JSON-serializable value."""
        return self.value


class SerializableEncoder(json.JSONEncoder):
    """JSON encoder that supports SerializableEnum members."""

    def default(self, o: Any) -> Any:
        if isinstance(o, SerializableEnum):
            return o.__json__()
        return super().default(o)
