"""manager"""
import time

from models.trolleybus import Trolleybus


def executiontime(func):
    """print function's execution time"""
    def timer(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Execution time: {end - start} seconds")
        return result

    return timer


def converter(func):
    """convert type, which is gotten from method, to tuple()"""
    def change_iterator(*args, **kwargs):
        func_res = func(*args, **kwargs)
        if isinstance(func_res, dict) and len(func_res) > 0:
            return tuple(func_res.items())
        return tuple(func(*args, **kwargs))

    return change_iterator


class TransportManager:
    """class contains list of Transport objects"""
    transports = []

    def __len__(self):
        return len(self.transports)

    def __getitem__(self, item):
        return self.transports[item]

    def __iter__(self):
        return iter(self.transports)

    @executiontime
    @converter
    def get_results(self):
        """return list of results of accelerate() method"""
        for temp in self.transports:
            temp.accelerate(30)
        return [result.current_speed for result in self.transports]

    @executiontime
    def get_enumerate_list_table(self):
        """return tuple of Transport objects with numeration"""
        return [(pos, type(transport).__name__ + ": " + str(transport))
                for pos, transport in enumerate(self.transports)]

    @executiontime
    def get_zip_list_table(self):
        """return tuple of Transport objects with accelerate() results"""
        for temp in self.transports:
            temp.accelerate(60)
        return [(type(transport).__name__ + ": " + str(transport), speed)
                for transport, speed in
                zip(self.transports,
                    [transport.current_speed for transport in self.transports])]

    @executiontime
    @converter
    def check_all_and_any(self):
        """return dictionary with keys(all, any)
        check if all/any Transport objects max_speed > 100"""
        return {'all': all(transport.max_speed > 100 for transport in self.transports),
                'any': any(transport.max_speed > 100 for transport in self.transports)}

    def add_transport(self, transport):
        """add transport to list"""
        self.transports.append(transport)

    @executiontime
    def find_all_with_id_greater_than(self, number):
        """get list <Transport> when id > number"""
        return [obj for obj in self.transports if obj.identifier > number]

    @executiontime
    def find_all_with_current_speed(self):
        """get list <Transport> when current_speed > number"""
        return [obj for obj in self.transports if obj.current_speed > 0]

    @executiontime
    def find_all_trolleybuses_with_passengers(self, number):
        """get list <Trolleybus> when passengers == number"""
        return [obj for obj in self.transports
                if isinstance(obj, Trolleybus) if obj.passengers is number]
