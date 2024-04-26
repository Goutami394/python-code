
class parent:
    def coolness(self):
        print("parents are cool")

class child1(parent):
    def coding(self):
         print("i know coding")
class child2(parent):
        def singing(self):
             print("i can sing")
anu=child1()
anu.coolness() 
anu.coding()  
anu=child2()     
rahul=child2()
rahul.coolness()
rahul.singing()