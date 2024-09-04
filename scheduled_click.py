from click import Click
from time_trigger import TimeTrigger

import sys
import keyboard
import mouse


class ScheduledClick(Click):
    def __init__(self, settings, type="left"):
        super().__init__(settings.position, type, settings.locked)
        settings.scheduler.add_job(
            self.click,
            TimeTrigger(settings.interval),
            args=[settings],
            id="click",
        )
        self.running = False
        self.settings = settings

    def start(self):
        self.settings.scheduler.start()
        self.running = True

    def pause(self, _):
        if self.running:
            self.settings.scheduler.pause_job("click")
            self.running = False
        else:
            self.settings.scheduler.resume_job("click")
            self.running = Truep

    def end(self, _):
        if self.running:
            self.settings.scheduler.remove_job("click")
            self.settings.scheduler.shutdown()
        keyboard.unhook_all()
        mouse.unhook_all()
        self.settings.scheduler.shutdown()
        sys.exit(0)
