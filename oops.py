class Animal():

    def __init__(self, legs, mouthsize, area, teeth, size, name, toes):
        self.legs = legs
        self.mouthsize = mouthsize
        self.area = area
        self.teeth = teeth
        self.size = size
        self.name = name
        self.toes = toes
    def fosssit (self):
        print(self.name)

class Fish(Animal):
    def __init__(self, legs, mouthsize, area, teeth, size, name, toes, tail, fins, beaks, food, robotic, speed):
        super().__init__(legs, mouthsize, area, teeth, size, name, toes)
        self.tail = tail
        self.fins = fins
        self.beaks = beaks
        self.food = food
        self.robotic = robotic
        self.speed = speed
scp918 = Fish("1", "35324m", "whole earth", "big sharp 50m, 19rows", "535325m", "scp918", "26", "nah", "10", "23", "people", "leg and water tank", 9876)
scp918.fosssit()

class Amphibian(Fish):
    def __init__(self,legs, mouthsize, area, teeth, size, name, toes, tail, fins, beaks, food, robotic, speed, eyes):
        super().__init__(legs, mouthsize, area, teeth, size, name, toes, tail, fins, beaks, food, robotic, speed)
        self.eyes = eyes
bloble = Amphibian("50", "25m", "Earth", "none", "45m", "bloble", "20", "1 short", "6", "none", "other fish and bacteria", "none", 5, "2")
bloble.fosssit()