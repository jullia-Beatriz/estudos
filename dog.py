class Dog():
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.energy = 3

    def latir(self):
        if self.energy > 0:
            self.energy -=  1
            print(f"{self.name} : auauauauauaua")
        else:
            print(f"{self.name} : rreeerererererere")
    
    def comer(self):
        if self.energy >= 3:
            print(f"{self.name} : huuuuummm")
        else:
            self.energy += 1
            print(f"{self.name} : nhecknhecknhecknheck")




doguinho = Dog("shuri", 1, "border collie")
doguinho1 = Dog("Rex", 2, "poddle")
doguinho2 = Dog("Chuchu", 3, "Pitbull")

doguinho1.latir()
doguinho1.latir()
doguinho1.latir()
doguinho1.latir()
doguinho1.comer()
doguinho1.comer()
doguinho.comer()
doguinho1.comer()
    