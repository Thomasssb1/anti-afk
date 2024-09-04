import sys
import keyboard
from settings import Settings
from scheduled_click import ScheduledClick

if __name__ == "__main__":
    
    settings = Settings(sys.argv[1:])

    print(
        "Recording mouse position, once hovering over the program window double click to confirm the target program"
    )
    settings.set_window()

    scheduled_click = ScheduledClick(settings)

    hook = keyboard.on_press_key(settings.key, scheduled_click.end)
    scheduled_click.start()
