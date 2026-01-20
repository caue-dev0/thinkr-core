from core.state import EditorState

def insert_text(state: EditorState, value: str) -> EditorState:
    lines = state.lines
    line = state.line
    col = state.col

    current_line =  lines[line]
    before = current_line[:col]
    after = current_line[col:]

    new_line = before + value + after

    new_lines = lines.copy()
    new_lines[line] = new_line

    return EditorState(
        lines=new_lines,
        line=line,
        col=col + len(value)
    )