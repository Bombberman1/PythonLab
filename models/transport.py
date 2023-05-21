"""classes"""
from abc import ABC, abstractmethod


class Transport(ABC):  # pylint: disable=too-few-public-methods
    """Abstract Transport"""

    # pylint: disable=too-many-arguments
    def __init__(self, identifier=0, max_speed=0, current_speed=0):
        self.identifier = identifier
        self.max_speed = max_speed
        self.current_speed = current_speed

    @abstractmethod
    def accelerate(self, speed):
        """changing current_speed"""
