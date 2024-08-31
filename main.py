import sys
import mouse
import keyboard
import time
import pygetwindow as gw
import random
from settings import Settings


def click(settings):
    window = settings.window
    if not window.isMaximized:
        window.restore()

    position = settings.position or (window.width / 2, window.height / 2)
    x, y = window.topleft.x + position[0], window.topleft.y + position[1]

    duration = random.random()
    mouse.move(x, y, absolute=True, duration=random.random())
    time.sleep(duration + 0.1)

    mouse.click("left")

    window.minimize()


if __name__ == "__main__":
    args = sys.argv[1:]
    settings = Settings(
        len(args) >= 1 and args[0] or "2s",
        len(args) >= 2 and args[1] or "q",
        len(args) >= 3 and args[2] or None,
    )

    print(
        "Recording mouse position, once hovering over the program window double click to confirm the target program"
    )

    def set_window():
        position = mouse.get_position()
        try:
            window = gw.getWindowsAt(position[0], position[1])[0]
            settings.setWindow(window)
        except:
            raise Exception("No window found at the position")

    hook = mouse.on_button(callback=set_window, buttons="left", types="double")
    mouse.wait(button="left", target_types="double")
    mouse.unhook(hook)

    while True:
        if keyboard.is_pressed(settings.key):
            break
        if settings.checkInterval():
            click(settings)
            settings.updateLastUsed()
