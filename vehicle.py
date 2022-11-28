class Vehicle():
    def __init__(self, brand, year, volume):
        self.brand = brand
        self.year = year
        self.volume = volume

    def check_tax(self):
        return print(((2022 - self.year) * self.volume)/100)


car1 = Vehicle('Toyota', 2004, 2700)
car2 = Vehicle('BMW', 1997, 3000)

car2.check_tax()