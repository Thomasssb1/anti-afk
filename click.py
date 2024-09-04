import mouse
from datetime import datetime
import pygetwindow as gw


class Click:
    def __init__(self, position, type, locked):
        self.position = position
        self.type = type
        self.locked = locked

    def update_position(self, position):
        if not self.locked:
            self.position = position

    def click(self, settings):
        if self.locked:
            try:
                if not settings.window.isActive:
                    settings.window.activate()
                settings.window.restore()

                settings.cache.set_position(mouse.get_position())

                position = settings.position or (
                    settings.window.width / 2,
                    settings.window.height / 2,
                )
                x, y = (
                    settings.window.topleft.x + position[0],
                    settings.window.topleft.y + position[1],
                )

                self.update_position((x, y))

                mouse.move(x, y, absolute=True)
                mouse.click(self.type)

                if settings.window.isActive:
                    settings.window.minimize()

                mouse.move(
                    settings.cache.lastPosition[0],
                    settings.cache.lastPosition[1],
                    absolute=True,
                )
            except gw.PyGetWindowException:
                raise Exception("Window not found, stopping script")
        else:
            mouse.click(self.type)
            
        if settings.verbose:
            print(f"TRIGGERED AT: {datetime.now()}")
            print(
                f"Clicked at: {x}, {y} in window: {settings.window.title}. Waiting for {settings.interval}."
            )
