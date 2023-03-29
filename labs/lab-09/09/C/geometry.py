class Circle:
    def __init__(self, center=Point(), radius=0):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f'Circle({self.center}, {self.radius})'

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

    def translate(self, dx, dy):
        return Circle(self.center.translate(dx, dy), self.radius)
