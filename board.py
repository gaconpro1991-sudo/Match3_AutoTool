from vision import recognize_cell

def build_board(board_img, rows, cols, cell_size, templates):
    matrix = []
    for r in range(rows):
        row = []
        for c in range(cols):
            cell = board_img.crop((
                c * cell_size,
                r * cell_size,
                (c + 1) * cell_size,
                (r + 1) * cell_size
            ))
            row.append(recognize_cell(cell, templates))
        matrix.append(row)
    return matrix
