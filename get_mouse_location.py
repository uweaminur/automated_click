from pynput.mouse import Listener
import pyautogui

def on_click(x, y, button, pressed):
    if pressed:
        # When a mouse button is pressed, get the current mouse position
        current_pos = pyautogui.position()
        print(f"Mouse clicked at position: {current_pos}")

# Set up the listener for mouse clicks
with Listener(on_click=on_click) as listener:
    listener.join()

