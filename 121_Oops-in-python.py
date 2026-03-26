class Mouse:
    def set_mouse(self,mouse_name,build_quality,mouse_color,mouse_price):
        self.name=mouse_name
        self.quality=build_quality
        self.color=mouse_color
        self.price=mouse_price
    def display_mouse(self):
        print("Mouse info:")
        print("Mouse name: ",self.name)
        print("Mouse quality: ",self.quality)
        print("Mouse color: ",self.color)
        print("Mouse price: ₹",self.price)
        print("---------------------------")

mouse1=Mouse()
mouse2=Mouse()
mouse3=Mouse()
mouse1.set_mouse("Zebronics","Plastic","RGB",599)
mouse2.set_mouse("Hp","Metal","Black",399)
mouse3.set_mouse("Intex","Plastic","White",249)
mouse1.display_mouse()
mouse2.display_mouse()
mouse3.display_mouse()