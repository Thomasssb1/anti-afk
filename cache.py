class Cache:
    def __init__(self, position):
        self.lastPosition = position
        
    def set_position(self, position):
        self.lastPosition = position