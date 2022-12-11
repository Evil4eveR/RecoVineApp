locations = [0,1]

class Draw:
    def __init__(self, locations):
        self.locations = locations

    def platforms(self):
        print(self.locations)

draw = Draw(locations)
draw.platforms()