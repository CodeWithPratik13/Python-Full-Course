class Animal:
    location = "australlia"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking Now...")


class Dog(Animal): # this is how inheritance is done inn python 
    def speak(self):
        super().speak()
        print("woof!")

d = Dog("Bruno")
d.speak()
# print(d.location)