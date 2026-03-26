class Lenovo:
    def set_laptop(self,lap_model,lap_processor,lap_GPU,lap_quality,lap_price):
        self.name=lap_model
        self.processor=lap_processor
        self.GPU=lap_GPU
        self.quality=lap_quality
        self.price=lap_price
    def display_it(self):
        print("Laptop info:")
        print("Model name: ",self.name)
        print("Processor: ",self.processor)
        print("GPU: ",self.GPU)
        print("Build quality: ",self.quality)
        print("Price: ₹",self.price)
        print("------------------")

model1=Lenovo()
model2=Lenovo()
model3=Lenovo()
model1.set_laptop("LOQ","i5","2050 Dedicated","soft Metal",55000)
model2.set_laptop("Thinkpad","i5","Integrated","Plastic",50000)
model3.set_laptop("Ideapad","i3","Integrated","Aluminium",59990)
model1.display_it()
model2.display_it()
model3.display_it()
