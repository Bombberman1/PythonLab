"""classes"""
from decorators.logged import logged
from exceptions.acceleration import OutOfLimitsError
from .transport import Transport


class Bus(Transport):
    """Bus"""

    transport_marks = {"Electron", "Bohdan", "Solaris"}

    # pylint: disable=too-many-arguments
    def __init__(self, identifier=0, max_speed=0, current_speed=0, windows=0):
        super().__init__(identifier, max_speed, current_speed)
        self.windows = windows

    @logged(OutOfLimitsError, "console")
    def accelerate(self, speed):
        """changing current_speed"""
        if speed > self.max_speed or speed < 0:
            raise OutOfLimitsError(speed)
        self.current_speed = speed

    def __str__(self):
        return f"{self.identifier} {self.max_speed} " \
               f"{self.current_speed} {self.windows}"

    def __repr__(self):
        return f"{self.identifier} {self.max_speed} " \
               f"{self.current_speed} {self.windows}"
