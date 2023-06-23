"""TransportManager's manager"""


class SetManager:
    """class has methods with TransportManager's list"""
    next_id = -1

    def __init__(self, transport_manager):
        self.transport_manager = transport_manager

    def __len__(self):
        return sum(len(transport.transport_marks) for transport
                   in self.transport_manager.transports)

    def __iter__(self):
        return self

    def __next__(self):
        self.next_id += 1
        if self.next_id >= len(self):
            self.next_id = -1
            raise StopIteration
        return [mark for transport in self.transport_manager.transports
                for mark in transport.transport_marks][self.next_id]

    def __getitem__(self, item):
        return [mark for transport in self.transport_manager.transports
                for mark in transport.transport_marks][item]
