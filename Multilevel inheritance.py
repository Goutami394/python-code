#multilevel inheritance
class parents:
    def coolness(self):
        print("parents are cool")

class child(parents):
    def coding(self):
         print("i know coding")
class child2(child):
        def singing(self):
             print("i can sing")
rahul=child2()
rahul.coolness()
rahul.coding()
rahul.singing()

