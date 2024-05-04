class Graph:
    def __init__(self):
        self.matrix={}
         #print(self.matrix)
    def addvertex(self,a,b):
        if a not in self.matrix:
            self.matrix[a]=[b]

        else:
            self.matrix[a].append(b)
    def print(self):
        print(self.matrix)
g=Graph()
g.addvertex(1,2)
g.addvertex(4,2)
g.addvertex(1,4)
g.addvertex(2,3)
g.addvertex(4,3)
g.print()
