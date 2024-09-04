from datetime import datetime, timedelta
from subprocess import Popen, PIPE
import pygetwindow as gw
from apscheduler.schedulers.blocking import BlockingScheduler as Scheduler
import mouse
import sys
import re
import math

from cache import Cache


class Settings:
    def __init__(self, args):
        parsed_args = Settings.parse_args(args)
        self.window = None
        self.interval = parsed_args["interval"]
        self.key = parsed_args["key"]
        self.pause_key = parsed_args["pause_key"]
        self.position = parsed_args["position"]
        self.locked = parsed_args["locked"]
        self.verbose = parsed_args["verbose"]
        self.cache = Cache(mouse.get_position())
        self.scheduler = Scheduler()

    @staticmethod
    def parse_args(args):
        args = sys.argv[1:]
        verbose = False
        if len(args) >= 1 and args[-1] == "-v":
            verbose = True
            args = args[:-1]
        return dict(interval= len(args) >= 1 and Settings.parse_interval(args[0]) or "10m", 
                key= len(args) >= 2 and args[1] or "q",
                pause_key = len(args) >= 3 and args[2] or "p",
                locked= Settings.parse_boolean(args[3]) if (len(args) >= 4 and args[3] != None) else True,
                position= len(args) >= 5 and Settings.parse_position(args[4]) or None, 
                verbose= verbose)

    @staticmethod
    def parse_boolean(value):
        if str.lower(value) == "true":
            return True
        elif str.lower(value) == "false":
            return False
        else:
            raise Exception("Invalid boolean format")

    @staticmethod
    def parse_position(position):
        if position == None:
            return
        try:
            newPosition = tuple(map(int, position.split(",")))
            return newPosition
        except:
            raise Exception("Invalid position format")

    @staticmethod
    def parse_interval(interval):
        try:
            newInterval = int(''.join(re.findall(r"^\d+", interval)))
            symbol = str.lower(interval[len(str(newInterval)):])
            if symbol == "ms":
                return timedelta(milliseconds=newInterval)
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

    def set_window(self):
        def find_window():
            position = mouse.get_position()
            try:
                self.window = gw.getWindowsAt(position[0], position[1])[0]
                print("Successfully set target window.")
            except:
                raise Exception("No window found at the position")

        hook = mouse.on_button(callback=find_window, buttons="left", types="double")
        mouse.wait(button="left", target_types="double")
        mouse.unhook(hook)
