import pyautogui
import os

def cap_name():
    captures = []
    count = []
    numbers = []

    for file in os.listdir():
        if file.startswith("capture"):
            captures.append(file)

    for cap in captures:
        numbers.clear()
        for char in cap:
            if char.isdigit():
                numbers.append(char)
        if len(numbers) > 0:
            count.append(int(''.join(numbers)))

    if len(captures) == 0:
        return "capture1.png"
    else:
        return "capture{0}.png".format(str(int(max(count)) + 1))

pyautogui.screenshot(cap_name());
