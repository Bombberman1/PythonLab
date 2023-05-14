class TrolleyBus:
    def __init__(self, identifier=150, route_number=0, current_stop=None, max_speed=0, current_speed=0, capacity=0,
                 passengers=0):
        self.identifier = identifier
        self.route_number = route_number
        self.current_stop = current_stop
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.capacity = capacity
        self.passengers = passengers

    def stop(self):
        self.current_speed = 0

    def start(self):
        self.current_speed = 20

    def add_passenger(self):
        if self.passengers < self.capacity:
            self.passengers += 1

    def remove_passenger(self):
        if self.passengers > 0:
            self.passengers -= 1

    def __str__(self):
        return f"{self.identifier} {self.route_number} {self.current_stop} {self.max_speed} " \
               f"{self.current_speed} {self.capacity} {self.passengers}"
