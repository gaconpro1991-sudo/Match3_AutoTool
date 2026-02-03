import pyautogui
import time
import random

def cell_to_xy(r, c, x, y, size):
    return x + c * size + size // 2, y + r * size + size // 2

def swap(p1, p2, x, y, size):
    x1, y1 = cell_to_xy(*p1, x, y, size)
    x2, y2 = cell_to_xy(*p2, x, y, size)

    pyautogui.click(x1, y1)
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.click(x2, y2)
