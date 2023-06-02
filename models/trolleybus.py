"""classes"""
from .transport import Transport


class Trolleybus(Transport):
    """Trolleybus"""

    transport_marks = {"Solaris", "Electron"}

    instance = None

    # pylint: disable=too-many-arguments
    def __init__(self, identifier=150, max_speed=0, current_speed=0,
                 route_number=0, current_stop="", capacity=0,
                 passengers=0):
        super().__init__(identifier, max_speed, current_speed)
        self.route_number = route_number
        self.current_stop = current_stop
        self.capacity = capacity
        self.passengers = passengers

    def accelerate(self, speed):
        """changing current_speed"""
        self.current_speed = speed

    @classmethod
    def get_instance(cls):
        """return def constructor"""
        if cls.instance is None:
            cls.instance = Trolleybus()
        return cls.instance

    def stop(self):
        """set speed 0"""
        self.current_speed = 0

    def start(self):
        """set speed 20"""
        self.current_speed = 20

    def add_passenger(self):
        """set passengers +1"""
        if self.passengers < self.capacity:
            self.passengers += 1

    def remove_passenger(self):
        """set passengers -1"""
        if self.passengers > 0:
            self.passengers -= 1

    def __str__(self):
        return f"{self.identifier} {self.max_speed} {self.current_speed} " \
               f"{self.route_number} {self.current_stop} {self.capacity} " \
               f"{self.passengers}"

    def __repr__(self):
        return f"{self.identifier} {self.max_speed} {self.current_speed} " \
               f"{self.route_number} {self.current_stop} {self.capacity} " \
               f"{self.passengers}"
