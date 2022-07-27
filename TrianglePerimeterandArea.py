class Triangle:
  def __init__(self, base, height, a, b, c):
    self.base = base
    self.height = height
    self.a = a
    self.b = b
    self.c = c

  def area(self):
    return self.base * self.height * 1//2

  def perimeter(self):
    return self.a + self.b + self.c
    
triangle1 = Triangle(10,20,30,40,50)
print("Triangle area is: " + str(triangle1.area()))
print("Triangle perimeter is: " + str(triangle1.perimeter()))
