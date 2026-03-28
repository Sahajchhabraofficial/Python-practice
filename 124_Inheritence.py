#multiple in heritance
class GasolineCars:
    def set_GCar(self,milage,price):
        self.milage=milage
        self.price=price
    
    def display_GCars(self):
        print("-----Gasoline Cars-----")
        print("Milage name: ",self.milage)
        print("Price: ",self.price)
class ElectricCars:
    def set_ECar(self,charge_power,Price):
        self.charge_power=charge_power
        self.Price=Price
    def display_ECars(self):
        print("-----Electric Car-----")
        print("Charge power: ",self.charge_power)
        print("price: ",self.Price)
class HybridCars(GasolineCars,ElectricCars):
    pass

        

Car1=HybridCars()
Car1.set_GCar(140,85000)
Car1.set_ECar(400,120000)
Car1.display_GCars()
Car1.display_ECars()