import json
class LogisticsRequest:
    id = None
    source = None
    destination = None
    weight = None
    zone = None
    rate = None
    status = 1

    def __init__(self, tour_obj):
        if 'id' in tour_obj:
            self.id = tour_obj['id']
        if 'source' in tour_obj:
            self.source = tour_obj['source']
        if 'destination' in tour_obj:
            self.destination = tour_obj['destination']
        if 'weight' in tour_obj:
            self.weight = tour_obj['weight']
        if 'zone' in tour_obj:
            self.zone = tour_obj['zone']
        if 'rate' in tour_obj:
            self.rate = tour_obj['rate']
        if 'status' in tour_obj:
            self.status = tour_obj['status']

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_source(self, source):
        self.source = source

    def set_destination(self, destination):
        self.destination = destination

    def set_weight(self, weight):
        self.weight = weight

    def set_zone(self, zone):
        self.zone = zone

    def set_rate(self, rate):
        self.rate = rate

    def set_status(self, status):
        self.status = status

    def get_id(self):
        return self.id

    def get_source(self):
        return self.source


    def get_destination(self):
        return self.destination

    def get_weight(self):
        return self.weight

    def get_zone(self):
        return self.zone

    def get_rate(self):
        return self.rate

    def get_status(self):
        return self.status
