class Animal: # This creates the parent class named Animal
  def __init__(self, name): # This initializes the animal and assigns its name
    self.name = name  # This stores the given name in the object's name attribute

  def eat(self): # This defines the eat method of the parent class
    print(f"{self.name} is eating.") # This displays the animal's eating behavior

          
  def make_sound(self): # This defines the make_sound method of the parent class
    print(f"{self.name} makes a sound.") # This displays the animal's sound

class Lion(Animal): # This creates the child class Lion that inherits from Animal
  def eat(self): # This defines the eat method of the parent class
    print(f"{self.name} eats fresh meat.") # This displays what the lion eats


  def make_sound(self): # This gives the make_sound method of the parent class
    print(f"{self.name} roars loudly!") # This displays the sound made by the lion

class Elephant(Animal): # This creates the child class Elephant that inherits from Animal
  def eat(self):  # This gives the eat method of the parent class
    print(f"{self.name} eats grass and fruits.") # This displays what the elephant eats

  def make_sound(self): # This gives the make_sound method of the parent class
    print(f"{self.name} trumpets!") # This displays the sound made by the elephant


class Monkey(Animal): # This creates the child class Monkey that inherits from Animal
    def eat(self): # This gives the eat method of the parent class
      print(f"{self.name} eats bananas.") # This displays what the monkey eats

    def make_sound(self): # This gives the make_sound method of the parent class
      print(f"{self.name} chatters!")   # This displays the sound made by the monkey

lion = Lion("Simba") # This creates a Lion object that has name called Simba
elephant = Elephant("Dumbo") # This creates an Elephant object that has a name called Dumbo
monkey = Monkey("George") # This creates a Monkey ob ject that has a name called George

lion.make_sound()
lion.eat()
print("-----")

elephant.make_sound()
elephant.eat()
print("-----")

monkey.make_sound()
monkey.eat()
print("-----")
