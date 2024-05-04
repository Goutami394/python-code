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
        def dfs(self,data):
            visited=[]
            stack=[data]
            while stack:
                vertex=stack.pop()
                print(vertex)
                if vertex in self.matrix:
                    for i in self.matrix[vertex]:
                        if i not in visited:
                            visited.append(i)
                            stack.append(i)
     
g=Graph()
g.addvertex(1,2)
g.addvertex(1,3)
g.addvertex(2,4)
g.addvertex(2,5)
g.addvertex(3,6)
g.addvertex(3,7)
g.dfs(1)
g.print()
