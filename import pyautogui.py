import pyautogui
import time

def auto_clicker(x, y, interval=10):
    """Move the mouse to a specific location (x, y) and click every specified interval (default is 10 seconds)."""
    try:
        while True:
            pyautogui.moveTo(x, y)  # Move the mouse to the specified coordinates
            pyautogui.click()       # Perform a click
            time.sleep(interval)    # Wait for the specified interval
    except KeyboardInterrupt:
        print("Program exited by user.")

# Set the coordinates for the mouse pointer (x, y) and interval
x_position = 500  # Change the x-coordinate as needed
y_position = 300  # Change the y-coordinate as needed
click_interval = 10  # Set the interval between clicks

auto_clicker(x_position, y_position, click_interval)
