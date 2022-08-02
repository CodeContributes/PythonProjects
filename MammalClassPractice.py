class Mammal:
  def __init__(self,animal,sound):
    self.animal = animal
    self.sound = sound

  def makeSound(self):
    return "A " + self.animal + " " + self.sound

class Cat(Mammal):
  def __init__(self,animal,sound):
    super().__init__(animal,sound)

class Dog(Mammal):
  def __init__(self,animal,sound):
    super().__init__(animal,sound)

class Horse(Mammal):
  def __init__(self,animal,sound):
    super().__init__(animal,sound)

animalList = [Cat('Cat','meows'), Dog('Dog','barks'), Horse('Horse','neighs')]

for i in  animalList:
  print(i.makeSound())
