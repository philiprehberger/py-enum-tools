# philiprehberger-enum-tools

Practical utilities for Python enums — lookup, validation, listing, and serialization.

## Install

```bash
pip install philiprehberger-enum-tools
```

## Usage

```python
from enum import Enum, auto
from philiprehberger_enum_tools import lookup, choices, values, names, validate

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
```

### Safe Lookup

```python
lookup(Color, "red")        # Color.RED
lookup(Color, "yellow")     # None
lookup(Color, "yellow", default=Color.RED)  # Color.RED
```

### Validation

```python
validate(Color, "red")      # Color.RED
validate(Color, "yellow")   # ValueError: 'yellow' is not a valid Color value. Valid values: 'red', 'green', 'blue'
```

### Listing

```python
values(Color)    # ['red', 'green', 'blue']
names(Color)     # ['RED', 'GREEN', 'BLUE']
choices(Color)   # [('red', 'RED'), ('green', 'GREEN'), ('blue', 'BLUE')]
```

### AutoEnum

Enum subclass where `auto()` generates lowercase member names as values.

```python
from philiprehberger_enum_tools import AutoEnum
from enum import auto

class Status(AutoEnum):
    ACTIVE = auto()
    INACTIVE = auto()
    PENDING = auto()

Status.ACTIVE.value   # 'active'
Status.PENDING.value  # 'pending'
```

### SerializableEnum

Enum that serializes to its value in JSON.

```python
import json
from philiprehberger_enum_tools import SerializableEnum, SerializableEncoder

class Priority(SerializableEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

json.dumps({"priority": Priority.HIGH}, cls=SerializableEncoder)
# '{"priority": 3}'
```

## API

| Function / Class | Description |
|---|---|
| `lookup(enum_class, value, *, default=None)` | Safe value-to-member lookup, returns default if not found |
| `choices(enum_class)` | List of (value, name) tuples for forms and CLIs |
| `values(enum_class)` | List of all member values |
| `names(enum_class)` | List of all member names |
| `validate(enum_class, value)` | Lookup or raise ValueError with valid options |
| `AutoEnum` | Enum subclass where auto() generates lowercase name as value |
| `SerializableEnum` | Enum that serializes to its value via SerializableEncoder |
| `SerializableEncoder` | JSON encoder supporting SerializableEnum members |

## License

MIT
