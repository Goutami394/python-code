#single inheritance
class parents:
    def coolness(self):
        print("parents are cool")
class child(parents):
    def coding(self):
        print("i know coding")
rahul=child()
rahul.coolness()
rahul.coding()