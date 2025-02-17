import pyautogui
import time

# Move the mouse to the top left corner of the screen
pyautogui.moveTo(0, 0, duration=2)  # Move over 2 seconds for visibility

# Move the mouse to a central location
screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2, duration=2)

# Test click
pyautogui.click()

