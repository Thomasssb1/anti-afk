import sys
import mouse
import pygetwindow as gw
import random
from settings import Settings


def click(window):
    if not window.isMaximized:
        window.restore()

    mouse.move(
        window.width / 2, window.height / 2, absolute=True, duration=random.random()
    )

    mouse.click("left")


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 0:
        raise Exception("No program name given")

    settings = Settings(
        args[0],
        len(args) >= 1 and args[1] or 15,
        len(args) >= 2 and args[2] or "q",
    )

    mouse.on_click(lambda: settings.updateLastUsed())
