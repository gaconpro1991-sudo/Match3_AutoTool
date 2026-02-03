import keyboard

auto_enabled = False

def toggle():
    global auto_enabled
    auto_enabled = not auto_enabled
    print("AUTO:", "ON" if auto_enabled else "OFF")

def setup():
    keyboard.add_hotkey("F8", toggle)
    keyboard.add_hotkey("esc", lambda: exit())
