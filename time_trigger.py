from apscheduler.triggers.base import BaseTrigger

class TimeTrigger(BaseTrigger):
    def __init__(self, interval):
        self.interval = interval
        
    def get_next_fire_time(self, previous_fire_time, now):
        return now + self.interval