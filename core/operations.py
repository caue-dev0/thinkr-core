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

def backspace(state: EditorState) -> EditorState:
    lines = state.lines
    line = state.line
    col = state.col

    if line == 0 and col == 0:
        return state
    
    if col > 0:
        current_line = lines[line]
        before = current_line[:col - 1]
        after = current_line[col:]

        new_line = before + after

        new_lines = lines.copy()
        new_lines[line] = new_line

        return EditorState(
            lines=new_lines,
            line=new_line,
            col=col -1
        )
    
    prev_line = lines[line - 1]
    current_line = lines[line]

    merged_line = prev_line + current_line

    new_lines = lines.copy()
    new_lines[line - 1] = merged_line
    new_lines.pop(line)

    return EditorState(
        lines=new_lines,
        line=new_line,
        col=len(prev_line)
    )

def enter(state: EditorState) -> EditorState:
    lines = state.lines
    line = state.line
    col = state.col

    current_line = lines[line]

    before = current_line[:col]
    after = current_line[col:]

    new_lines = lines.copy()
    new_lines[line] = before
    new_lines.insert(line + 1, after)

    return EditorState(
        lines=new_lines,
        line=line + 1,
        col=0
    )

def move_left(state: EditorState) -> EditorState:
    lines = state.lines
    line = state.line
    col = state.col

    if line == 0 and col == 0:
        return state
    
    if col > 0:
        return  EditorState(
            lines=lines,
            line=line,
            col=col - 1
        )
    
    prev_line_len = len(lines[line - 1])
    return EditorState(
        lines=lines,
        line=line - 1,
        col=prev_line_len
    )

def move_right(state: EditorState) -> EditorState:
    lines = state.lines
    line = state.line
    col = state.col

    current_line = lines[line]

    if col < len(current_line):
        return EditorState(
            lines=lines,
            line=line,
            col=col + 1
        )
    
    if line < len(lines) - 1:
        return EditorState(
            lines=lines,
            line=line + 1,
            col=0
        )

    return state

def move_up(state: EditorState) -> EditorState:
    lines = state.lines
    line = state.line
    col = state.col

    if line == 0:
        return state
    
    new_line = line - 1
    new_col = min(col, len(lines[new_line]))

    return EditorState(
        lines=lines,
        line=new_line,
        col=new_col
    )

def move_down(state: EditorState) -> EditorState:
    lines = state.lines
    line = state.line
    col = state.col

    if line >= len(lines) - 1:
        return state
    
    new_line = line + 1
    new_col = min(col, len(lines[new_line]))

    return EditorState(
        lines=lines,
        line=new_line,
        col=new_col
    )