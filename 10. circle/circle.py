import math

class Circle(object):
    """A class representation of a circle shrug for days.
    """
    def __init__(self, radius=1):
        """Circle constructor"""
        self._radius = radius

    def __repr__(self):
        """Circle nice string representation"""
        return "Circle({})".format(self.radius)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self._radius = value

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        """Diameter setter"""
        self._radius = value/2

    @property
    def area(self):
        return math.pi*math.pow(self.radius, 2)

    @area.setter
    def area(self, value):
        raise AttributeError()

if __name__ == "__main__":
    c = Circle(5)
    print(c.radius)
    c.diameter = 50
    print(c.radius)
