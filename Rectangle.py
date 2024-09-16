class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def get_dimensions(self):
        return [{"length": self.length}, {"width": self.width}]
    
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

rect = Rectangle(length, width)
print(rect.get_dimensions())
