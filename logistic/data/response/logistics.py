
import json
class Logistics_Response:
    id = None
    city = None
    part = None
    source = None
    source_name = None
    destination = None
    destination_name = None
    weight = None
    zone = None
    rate = None
    status = 1
    data = []

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_city(self, city):
        self.city = city

    def set_part(self, part):
        self.part = part

    def set_source(self, source):
        self.source = source

    def set_sourcename(self, source_name):
        self.source_name = source_name

    def set_destination(self, destination):
        self.destination = destination

    def set_destinationname(self, destination_name):
        self.destination_name = destination_name

    def set_weight(self, weight):
        self.weight = weight

    def set_zone(self, zone):
        self.zone = zone

    def set_rate(self, rate):
        self.rate = rate

    def set_status(self, status):
        self.status = status

    def set_data(self, data):
        self.data = data

    def get_id(self):
        return self.id

    def get_city(self):
        return self.city

    def get_part(self):
        return self.part

    def get_source(self):
        return self.source

    def get_sourcename(self):
        return self.source_name

    def get_destination(self):
        return self.destination

    def get_destinationname(self):
        return self.destination_name

    def get_weight(self):
        return self.weight

    def get_zone(self):
        return self.zone

    def get_rate(self):
        return self.rate

    def get_status(self):
        return self.status

    def get_data(self):
        return self.data
