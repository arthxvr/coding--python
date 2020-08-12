class Cube(object):
    def __init__(self, edge):
        self.edge = edge
        
    def area(self):
        return self.edge ** 2
    
    def volume(self):
        return (self.edge ** 2) * 6
    
c = Cube(4)
print('Area: ', c.area())
print('Volume: ', c.volume())
