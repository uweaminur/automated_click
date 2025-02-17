import pyautogui
import time

def auto_clicker(x, y, interval=5):
    """Move the mouse to a specific location (x, y) and click every specified interval (default is 5 seconds)."""
    try:
        while True:
            pyautogui.moveTo(x, y, duration=1)  # Move the mouse to the specified coordinates
            pyautogui.click()                   # Perform a click
            time.sleep(interval)                # Wait for the specified interval
    except KeyboardInterrupt:
        print("Program exited by user.")

# Set the coordinates for the mouse pointer (x, y) and interval
x_position = 1069  # x-coordinate where the click should occur
y_position = 523   # y-coordinate where the click should occur
click_interval = 0.25  # Set the interval between clicks in seconds

auto_clicker(x_position, y_position, click_interval)

