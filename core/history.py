from dataclasses import dataclass
from core.state import EditorState

@dataclass(frozen=True)
class History:
    past: list[EditorState]
    present: EditorState
    future: list[EditorState]

def create_history(state: EditorState) -> History:
    return History(
        past=[],
        present=state,
        future=[]
    )