import time
from config import *
from capture import capture_board
from vision import load_templates
from board import build_board
from solver import smart_best_move
from controller import swap
from hotkey import setup, auto_enabled

setup()
templates = load_templates()

print("F8: BẬT / TẮT AUTO | ESC: THOÁT")

while True:
    if auto_enabled:
        img = capture_board(BOARD_X, BOARD_Y, CELL_SIZE * ROWS)
        board = build_board(img, ROWS, COLS, CELL_SIZE, templates)
        move = smart_best_move(board)
        if move:
            swap(move[0], move[1], BOARD_X, BOARD_Y, CELL_SIZE)
            time.sleep(0.25)
    else:
        time.sleep(0.1)
