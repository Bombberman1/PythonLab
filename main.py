"""main"""
from managers.transport_manager import transports, add_transport, find_all_with_id_greater_than, \
    find_all_with_current_speed, find_all_trolleybuses_with_passengers
from models.bus import Bus
from models.car import Car
from models.motor_bike import MotorBike
from models.trolleybus import Trolleybus

# adding Transport objects to list
add_transport(Trolleybus(50, 80, 0, 13, "Lviv", 30, 10))
add_transport(Car(78, 4, 120, 30, 50, 600, 90))
add_transport(Car(21, 2, 80, 0, 20, 400, 120))
add_transport(Trolleybus(47, 90, 40, 39, "Kyiv", 30, 20))
add_transport(Bus(140, 12, 80, 20))
add_transport(Bus())
add_transport(MotorBike(90, 130, 15, True))
add_transport(MotorBike())

print('-' * 30)
for transport in transports:
    print(transport)
print('-' * 30)

for i in find_all_with_id_greater_than(70):
    print(i)
print('-' * 30)

for i in find_all_with_current_speed():
    print(i)
print('-' * 30)

for i in find_all_trolleybuses_with_passengers(10):
    print(i)
print('-' * 30)
