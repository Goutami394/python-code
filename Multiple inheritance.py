
class dad:
    def coolness(self):
        print("parents are cool")

class mom:
    def coding(self):
         print("i know coding")
class child2(dad,mom):
        def singing(self):
             print("i can sing")
        
rahul=child2()
rahul.coolness()
rahul.coding()
rahul.singing()