from core.state import EditorState
from core.actions import *
from core import operations as ops

def dispatch_state(state: EditorState, action: Action) -> EditorState:
    match action:
        case Insert(value=value):
            return ops.insert_text(state, value)
        
        case Backspace():
            return ops.backspace(state)
        
        case Enter():
            return ops.backspace(state)
        
        case Delete():
            return ops.delete(state)
        
        case MoveLeft():
            return ops.move_left(state)
        
        case MoveRight():
            return ops.move_right(state)
        
        case MoveUp():
            return ops.move_up(state)
        
        case MoveDown():
            return ops.move_down(state)
        
        case Home():
            return ops.move_home(state)
        
        case End():
            return ops.move_end(state)
        
        case _:
            return state