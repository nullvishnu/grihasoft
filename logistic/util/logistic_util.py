

class City_Part:
    North = 1
    South = 2
    East  = 3
    West  = 4

    def get_part(self, id):
        if id == 1:
            return "North"
        elif id == 2:
            return "South"
        elif id == 3:
            return "East"
        elif id == 4:
            return "West"

    def get_id(self, data):
        if data == "North":
            return 1
        elif data == "South":
            return 2
        elif data == "East":
            return 3
        elif data == "West":
            return 4