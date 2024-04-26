
class parent:
    def coolness(self):
        print("parents are cool")

class child1(parent):
    def coding(self):
            print("i know coding")
class child2(parent):
        def singing(self):
             print("i can sing")
class grandchild(child1,child2):
      def dancing(self):
            print("i can dance")
anu=grandchild()
anu.coolness() 
anu.coding() 
anu.singing()
anu.dancing() 
    
rahul=child2()
rahul.coolness()
rahul.singing()