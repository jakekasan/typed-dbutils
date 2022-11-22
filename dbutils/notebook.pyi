
from typing import Any, Dict


def run(path: str, timeout_seconds: int, arguments: Dict[Any, Any]) -> str:
    ...

def exit(value: str) -> None:
    ...
