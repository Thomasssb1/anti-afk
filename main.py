import sys
import mouse
import keyboard
import time
import pygetwindow as gw
import random
from apscheduler.schedulers.blocking import BlockingScheduler as Scheduler
from time_trigger import TimeTrigger
from settings import Settings
from cache import Cache


def click(settings, cache):
    try:
        window = settings.window
        if not window.isActive:
            window.restore()
            
        cache.set_position(mouse.get_position())

        position = settings.position or (window.width / 2, window.height / 2)
        x, y = window.topleft.x + position[0], window.topleft.y + position[1]

        duration = random.random()
        mouse.move(x, y, absolute=True, duration=random.random())
        time.sleep(duration + 0.1)

        mouse.click("left")

        if window.isActive:
            window.minimize()
        
        if settings.verbose:
            print(f"TRIGGERED AT: {settings.lastUsed}")
            print(
                f"Clicked at: {x}, {y} in window: {window.title}. Waiting for {settings.interval}."
            )
        time.sleep(3)
        mouse.move(cache.lastPosition[0], cache.lastPosition[1], absolute=True)
        
    except gw.PyGetWindowException:
        raise Exception("Window not found, stopping script")

if __name__ == "__main__":
    args = sys.argv[1:]
    verbose = False
    if len(args) >= 1 and args[-1] == "-v":
        verbose = True
        args = args[:-1]
    settings = Settings(
        len(args) >= 1 and args[0] or "10m",
        len(args) >= 2 and args[1] or "q",
        len(args) >= 3 and args[2] or None,
        verbose,
    )

    print(
        "Recording mouse position, once hovering over the program window double click to confirm the target program"
    )

    def set_window():
        position = mouse.get_position()
        try:
            window = gw.getWindowsAt(position[0], position[1])[0]
            settings.setWindow(window)
            print("Successfully set target window.")
        except:
            raise Exception("No window found at the position")

    hook = mouse.on_button(callback=set_window, buttons="left", types="double")
    mouse.wait(button="left", target_types="double")
    mouse.unhook(hook)
    
    cache = Cache(mouse.get_position())

    def kill_sched(sched):
        sched.remove_job("click")
        sched.shutdown()

    sched = Scheduler()

    hook = keyboard.on_press_key(settings.key, lambda a: kill_sched(sched))
    
    trigger = TimeTrigger(settings.interval)
    sched.add_job(
        click, trigger, args=[settings, cache], id="click"
    )

    sched.start()


