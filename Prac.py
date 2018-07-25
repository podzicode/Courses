class Vehicle:
    def __init__(self,body,make,year,wheels):
        self.body=body;
        self.make=make;
        self.year=year
        self.wheels=wheels
    def  price(self):
        price=self.wheels*100
        return price;
class Skoda(Vehicle):
    def __init__(self,body,make,year,wheels,tag,logo):
        Vehicle.__init__(self,body,make,year,wheels)
        self.tag=tag
        self.logo=logo
S1= Skoda(12,32,12,33,24,5)
nm=S1.price();
print nm

