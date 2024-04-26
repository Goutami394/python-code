class queue:
    def __init__(self):
        self.rear=self.front=-1
        self.size=5
        self.list=[]
    def enqueue(self,data):
        if len(self.list)==5:
            print("full")
            return 0
        self.rear+=1
        self.list.append(data)
        if self.front==-1:
            self.front+=1
    def dqueue(self):
        if len(self.list)==0:
            print("empty")
            return 0
        self.list.pop(0)
        self.front+=1
    def display(self):
        if len(self.list)==0:
            print("empty")
            return 0
        print(self.list)
q=queue()
q.enqueue(5)
q.enqueue(7)
q.enqueue(8)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
q.dqueue()
q.display()
