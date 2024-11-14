def number(lines):
    text_editor_lines = []
    if not lines:
        return []
    for i,line_text in enumerate(lines):
        text_editor_lines.append(f'{i+1}: {line_text}')
    return text_editor_lines