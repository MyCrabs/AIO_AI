class Bird():
    def fly(self):
        print("Fly with Swing")
        
class Airplane():
    def fly(self):
        print("Fly with Fuel")
        
class Fish():
    def swim(self):
        print("Swimmm")

for obj in Bird(), Airplane(), Fish():
    obj.fly()