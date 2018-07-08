class V0Circle:
    """Circle with radius, area, diameter.

    This answer doesn't really work.

    Missing two features:
        - Default radius to 1
        - Nice string representation
    """
    def __init__(self, radius):
        self.radius = radius
        self.area = math.pi * self.radius ** 2
        self.diameter = self.radius * 2

class V1Circle:
    """Circle with radius, area, diameter.

    Adding the string representation. Using 'f' for string formatting
    is only available in python3.

    Defaulting radius to 1.
    """
    def __init__(self, radius=1):
        self.radius = radius
        self.area = math.pi * self.radius ** 2
        self.diameter = self.radius * 2

    def __repr__(self):
        return f'Circle({self.radius})'

class V2Circle:
    """Circle with radius, area, and diameter.

    Making area and diamter a property.
    """

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return f'Circle({self.radius})'

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

class V3Circle:
    """Circle with radius, area, and diameter.

    Updating radius when updating the diameter.
    Adding a setter to the diameter property.
    """

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return f'Circle({self.radius})'

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

class V4Circle:
    """Circle with radius, area, and diameter.

    Making radius a property. Raising exception for negative values.
    """

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return f'Circle({self.radius})'

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius
