class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def delta_x(self, d):
        return Point(self.x + d, self.y)

    def delta_y(self, d):
        return Point(self.x, self.y + d)

    def translate(self, dx, dy):
        return Point(self.x + dx, self.y + dy)
