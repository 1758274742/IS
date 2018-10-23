class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

class Square(Rectangle):

    def __init__(self, width):
        self.width  = width
        self.height = width

class Ellipse(Rectangle): 
    def __init__(self, width, height):
        self.width = 3.14*width
        self.height = height
  
class Circle(Rectangle):       
    def __init__(self, width):
        self.width = 3.14*width
        self.height = width

 
def compute_area(shapes):
    return  sum([x.area() for x in shapes])
