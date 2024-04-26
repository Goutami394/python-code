class MyQueue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def push(self,x:int)->None:
        self.s1.append(x)
    def pop(self)->int:
        for i in range(len(self.s1)):
            self.s2.append(self.s1.pop())
        a=self.s2.pop()
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        return a
    def peek(self)->int:
        return self.s1[0]
    def empty(self)->bool:
        if len(self.s1)==0:
            return True
        else:
            return False