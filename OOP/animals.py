# this illustrates design first implementation

class Animal:
    """
    animal class

    Attributes:
        DEFAULT_STATUS:  a defaut status for all animals -> alive
        name: animal name
        sound: speach from animal
        status: current state of animal
        children: int if animal has childern

    methods:
        move: change location of animal
        speak: make animal talk
        eat: animal should eat
    """

    DEFAULT_STATUS = "alive"

    def __init__(self, name: str, children: int, sound: str) -> None:
        self.name = name
        self.sound = sound
        self.children = children
        self.status =  self.DEFAULT_STATUS
    
    def speak(self):
        print(f"{self.name} says {self.sound}")
    def poop(self):
        pass
    def eat(self):
        pass
    
    # a private method
    def __tuckin(self):
        pass

def profile_animal(animal: Animal):
    print(animal.name)
    print(animal.children)
    print(animal.sound)
    print(animal.status)
def care_for(animal: Animal):
    animal.speak()
def kill(animal: Animal):
    animal.status = "DEAD"
    animal.speak()
def eat_animal(animal: Animal):
    print(f"{animal.name} was yummy")



#  simulate animals

dog = Animal("dog", children = 0, sound = "woof")

profile_animal(dog)
care_for(dog)
kill(dog)
profile_animal(dog)



