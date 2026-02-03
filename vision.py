import cv2
import numpy as np
import os
import sys

def resource_path(relative):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative)

def load_templates():
    templates = {}
    path = resource_path("assets/icons")
    for f in os.listdir(path):
        img = cv2.imread(os.path.join(path, f))
        if img is not None:
            templates[f.split(".")[0]] = img
    return templates

def recognize_cell(cell, templates):
    cell = cv2.cvtColor(np.array(cell), cv2.COLOR_RGB2BGR)
    for k, temp in templates.items():
        res = cv2.matchTemplate(cell, temp, cv2.TM_CCOEFF_NORMED)
        if res.max() > 0.75:
            return k
    return None
