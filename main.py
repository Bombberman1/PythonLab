"""main"""
from managers.transport_manager import TransportManager
from managers.set_manager import SetManager
from models.bus import Bus
from models.car import Car
from models.motor_bike import MotorBike
from models.trolleybus import Trolleybus

tm = TransportManager()
# adding Transport objects to list
tm.add_transport(Trolleybus(50, 80, 0, 13, "Lviv", 30, 10))
tm.add_transport(Car(78, 120, 30, 4, 50, 600, 90))
tm.add_transport(Car(21, 80, 0, 2, 20, 400, 120))
tm.add_transport(Trolleybus(47, 90, 40, 39, "Kyiv", 30, 20))
tm.add_transport(Bus(140, 80, 12, 20))
tm.add_transport(Bus())
tm.add_transport(MotorBike(90, 130, 15, True))
tm.add_transport(MotorBike())

print('-' * 30)
for transport in tm.transports:
    print(transport)
print('-' * 30)

for i in tm.find_all_with_id_greater_than(70):
    print(i)
print('-' * 30)

for i in tm.find_all_with_current_speed():
    print(i)
print('-' * 30)

for i in tm.find_all_trolleybuses_with_passengers(10):
    print(i)
print('-' * 30)

print(len(tm))
print('-' * 30)
print(tm[0])
print('-' * 30)
tm_iter = iter(tm)
for i in range(8):
    print(next(tm_iter))
print('-' * 30)
print(tm.get_results())
print('-' * 30)
for i in tm.get_enumerate_list_table():
    print(i)
print('-' * 30)
for i in tm.get_zip_list_table():
    print(i)
print('-' * 30)
for i in tm.transports:
    print(i.get_dict_with_type(str))
print('-' * 30)
print(tm.check_all_and_any())
print('-' * 30)
for i in tm.transports:
    print(i.transport_marks)
print('-' * 30)

sm = SetManager(tm)
print(len(sm))
print('-' * 30)
sm_iter = iter(sm)
for i in range(22):
    print(next(sm_iter))
print('-' * 30)
print(sm[21])
print('-' * 30)
