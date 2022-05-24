class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passenger_list = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passenger_list)

    def pick_up(self, passenger):
        self.passenger_list.append(passenger)

    def drop_off(self, passenger):
        self.passenger_list.remove(passenger)

    def empty(self):
        self.passenger_list -= self.passenger
        # self.pick_up(self.passenger)
        # self.pick_up(self.passenger)
        # len(self.passenger_list)
