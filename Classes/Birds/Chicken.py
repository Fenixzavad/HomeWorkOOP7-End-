from ..Interfece.BirdFly import BirdFly
from .Bird import Bird

class Chicken(Bird, BirdFly):
    def __init__(self, name, height, weight, colorEye, fly):
        super().__init__(name, height, weight, colorEye, fly)

    def animalSay(self):
        print(f"{super().animalSay()} 'Кудах-тах-тах'")

    def birdFly(self):
        BirdFly.birdFly(self)

    def __str__(self) -> str:
        return super().__str__()