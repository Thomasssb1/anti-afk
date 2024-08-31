from datetime import datetime
from subprocess import Popen, PIPE
import pygetwindow as gw


class Settings:
    def __init__(self, programName, interval, keyToStop):
        self.interval = interval
        self.key = keyToStop
        self.programName = programName
        self.lastUsed = datetime.now()

    def checkInterval(self):
        if (datetime.now() - self.lastUsed).total_seconds() // 60 >= self.interval:
            return True

    def updateLastUsed(self):
        self.lastUsed = datetime.now()

    def findWindow(self):
        window = gw.getWindowsWithTitle(self.programName)
        if len(window) == 0:
            raise Exception("No window found with the given name")
        return window[0]
