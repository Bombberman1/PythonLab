"""classes"""
from .transport import Transport


class Car(Transport):
    """Car"""

    # pylint: disable=too-many-arguments
    def __init__(self, identifier=0, max_speed=0, current_speed=0,
                 doors=0, trunk_volume=0, max_weight=0,
                 current_weight=0):
        super().__init__(identifier, max_speed, current_speed)
        self.doors = doors
        self.trunk_volume = trunk_volume
        self.max_weight = max_weight
        self.current_weight = current_weight

    def accelerate(self, speed):
        """changing current_speed"""
        super().current_speed = speed

    def __str__(self):
        return f"{self.identifier} {self.max_speed} {self.current_speed} " \
               f"{self.doors} {self.trunk_volume} {self.max_weight} " \
               f"{self.current_weight}"
