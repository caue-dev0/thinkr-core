from core.history import History
from core.actions import *
from core.dispatch_state import dispatch_state

def dispatch_history(history: History, action: Action) -> History:
    past = history.past
    present = history.present
    future = history.future

    # Undo
    if isinstance(action, Undo):
        if not past:
            return history
        
        return History(
            past=past[:-1],
            present=past[:-1],
            future=[present] + future
        )
    
    # Redo
    if isinstance(action, Redo):
        if not future:
            return history
        
        return History(
            past=past + [present],
            present=future[0],
            future=future[1:]
        )
    
    new_state = dispatch_state(present, action)

    if new_state == present:
        return history
    
    return history(
        past=past + [present],
        present=new_state,
        future=[]
    )