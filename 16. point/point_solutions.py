class v0_Point:

    """Three-dimensional point."""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        """Return dev-readable representation of Point."""
        return "Point({}, {}, {})".format(self.x, self.y, self.z)

    def __eq__(self, other):
        """Return True if our point is equal to the other point."""
        return self.x == other.x and self.y == other.y and self.z == other.z

class v1_Point:

    """Three-dimensional point."""

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        """Return dev-readable representation of Point."""
        return f"Point({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        """Return True if our point is equal to the other point."""
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    """Bonus 1: allow point objects to added to and subtracted from each other.
    """
    def __add__(self, other):
        """Return copy of our point, shifted by other."""
        return Point(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        """Return copy of our point, shifted by other."""
        return Point(self.x-other.x, self.y-other.y, self.z-other.z)

    """Bonus 2: allow point objects to work with multiplication."""
    def __mul__(self, scalar):
        """Return new copy of our point, scaled by given value."""
        return Point(scalar*self.x, scalar*self.y, scalar*self.z)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    """Bonus 3: alllow points to work with multiple assignment (tuple unpacking).
    """
    def __iter__(self):
        return iter((self.x, self.y, self.z))
