class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("drivee")

class boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("saill")

class plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("flyyy")


car1=car("ford","mustang")
boat1=boat("ibla","touriing1")
plane1=plane("bodud","747")

for x in(car1,boat1,plane1):
    x.move()

