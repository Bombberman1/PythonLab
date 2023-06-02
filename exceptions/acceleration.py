"""my exceptions"""


class OutOfLimitsError(Exception):
    """exception class for models acceleration"""
    def __init__(self, speed="speed"):
        self.speed = speed

    def __str__(self):
        return f"{self.speed} < 0 or {self.speed} > max speed"

    def __repr__(self):
        return f"{self.speed} < 0 or {self.speed} > max speed"
