from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class EditorState:
    lines: List[str]
    line: int
    col: int

def create_state(text: str = "") -> EditorState:
    lines = text.split("\n")
    return EditorState(
        lines=lines if lines else [""],
        line=0,
        col=0
    )