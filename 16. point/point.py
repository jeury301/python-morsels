class Point(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "Point({x}, {y}, {z})".format(x=self.x,y=self.y,z=self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y,self.z+other.z)

    def __sub__(self, other):
        return Point(self.x-other.x,self.y-other.y,self.z-other.z)

    def __mul__(self,factor):
        return Point(self.x*factor,self.y*factor,self.z*factor)

    def __rmul__(self, factor):
        return Point(self.x*factor,self.y*factor,self.z*factor)

    def __iter__(self):
        return iter([self.x,self.y,self.z])

if __name__ == "__main__":
    p1 = Point(1,2,3) * 3
    p1 = 3 * p1
    print(p1)
