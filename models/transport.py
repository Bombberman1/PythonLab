"""classes"""
from abc import ABC, abstractmethod


class Transport(ABC):  # pylint: disable=too-few-public-methods
    """Abstract Transport"""
    transport_marks = {}

    # pylint: disable=too-many-arguments
    def __init__(self, identifier=0, max_speed=0, current_speed=0):
        self.identifier = identifier
        self.max_speed = max_speed
        self.current_speed = current_speed

    # pylint: disable=unidiomatic-typecheck
    def get_dict_with_type(self, value_type):
        """return dictionary of attributes"""
        return {key: value for key, value in self.__dict__.items()
                if type(value) is value_type}

    def __iter__(self):
        return iter(self.transport_marks)

    @abstractmethod
    def accelerate(self, speed):
        """changing current_speed"""
