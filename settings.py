from datetime import datetime, timedelta
from subprocess import Popen, PIPE
import pygetwindow as gw


class Settings:
    def __init__(self, interval, keyToStop, position):
        self.window = None
        self.interval = Settings.parseInterval(interval)
        self.key = keyToStop
        self.position = Settings.parsePosition(position)
        self.lastUsed = datetime.now()

    def parsePosition(position):
        if position == None:
            return
        try:
            newPosition = tuple(map(int, position.split(",")))
            return newPosition
        except:
            raise Exception("Invalid position format")

    def parseInterval(interval):
        try:
            symbol = str.lower(interval[-1])
            newInterval = int(interval[:-1])
            if symbol == "s":
                return timedelta(seconds=newInterval)
            elif symbol == "m":
                return timedelta(minutes=newInterval)
            elif symbol == "h":
                return timedelta(hours=newInterval)
            else:
                raise Exception("Invalid interval format")
        except:
            raise Exception("Invalid interval format")

    def checkInterval(self):
        if (datetime.now() - self.lastUsed) >= self.interval:
            return True

    def updateLastUsed(self):
        self.lastUsed = datetime.now()

    def setWindow(self, window):
        self.window = window
