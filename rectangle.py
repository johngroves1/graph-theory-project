
class Rectangle:
    # Constructor.
    def __init__(self, height, width):
        self.height = height
        self.width = width
    # Calculate the area.
    def area(self):
        a = self.height * self.width
        return a
    # Calculate the perimeter.
    def perimeter(self):
        p = (2 * self.height) + (2 * self.width)
        return p


# Create instance.
r1 = Rectangle(10, 35)

# Another instance.
r2 = Rectangle(2, 5)

print(f"Area of r1 = {r1.height} x {r1.width} = {r1.area()}")
print("The area of the other rectangle is", r2.area())
print("The perimeter of the other rectangle is", r2.perimeter())

