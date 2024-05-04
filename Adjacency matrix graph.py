class Graph:
      def __init__(self):
         self.matrix=[[0]*5 for i in range(5)]
         #print(self.matrix)
      def addvertex(self,a,b):
           self.matrix[a][b]=1
      def print(self):
           for i in self.matrix:
                print(i)
                
g=Graph()
g.addvertex(1,2)
g.addvertex(4,2)
g.addvertex(1,4)
g.addvertex(2,3)
g.addvertex(4,3)
g.print()
