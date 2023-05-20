"""main"""
from trolleybus import Trolleybus


trolleybuses = {
    Trolleybus(),
    Trolleybus(42, 10, "Lviv", 120, 60, 20, 10),
    Trolleybus.get_instance(),
    Trolleybus.get_instance(),
}
for transport in trolleybuses:
    print(transport)
