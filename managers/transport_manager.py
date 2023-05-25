"""manager"""
from models.trolleybus import Trolleybus

transports = []


def add_transport(transport):
    """add transport to list"""
    transports.append(transport)


def find_all_with_id_greater_than(number):
    """get list <Transport> when id > number"""
    return [obj for obj in transports if obj.identifier > number]


def find_all_with_current_speed():
    """get list <Transport> when current_speed > number"""
    return [obj for obj in transports if obj.current_speed > 0]


def find_all_trolleybuses_with_passengers(number):
    """get list <Trolleybus> when passengers == number"""
    return [obj for obj in transports if isinstance(obj, Trolleybus) if obj.passengers is number]
