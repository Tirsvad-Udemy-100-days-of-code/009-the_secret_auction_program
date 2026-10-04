"""! @file env.py
@brief Minimal `.env` file loader using only the standard library.
"""

import os
from pathlib import Path


def parse_env(text: str) -> dict[str, str]:
    """! @brief Parse `KEY=VALUE` lines.
    @param text Contents of a `.env` file. Blank lines and `#` comments are ignored.
    @return Dictionary of parsed variables; surrounding quotes are stripped.
    """
    values: dict[str, str] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        values[key.strip()] = value
    return values


def load_env(path: str | Path) -> dict[str, str]:
    """! @brief Load a `.env` file into `os.environ` without overriding existing variables.
    @param path Path to the `.env` file; a missing file is not an error.
    @return Dictionary of the variables read from the file.
    """
    file = Path(path)
    if not file.is_file():
        return {}
    values = parse_env(file.read_text(encoding="utf-8"))
    for key, value in values.items():
        os.environ.setdefault(key, value)
    return values
