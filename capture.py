import pyautogui
from PIL import Image

def capture_board(x, y, size):
    screenshot = pyautogui.screenshot()
    board = screenshot.crop((x, y, x + size, y + size))
    return board
