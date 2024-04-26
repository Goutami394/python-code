
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insertatbeg(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head 
            self.head=newnode

    def insertatend(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=newnode
    def count(self):
        count=0
        if self.head==None:
            print("not found")
        else:
            curr=self.head
            while curr!=None:
                count+=1
                curr=curr.next
            print(count)
    def insertmid(self,val):
        newnode=Node(val)
        count=0
        if self.head==None:
            self.head=newnode
        elif self.head.next==None:
            self.head.next=newnode
        else:
            curr=self.head
            while curr!=None:
                count+=1
                curr=curr.next
            curr=self.head
            for i in range(count//2):
                curr=curr.next
            newnode.next=curr.next
            curr.next=newnode
    def middle(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        elif self.head.next==None:
            self.head.next=newnode
        else:
            fast=self.head
            slow=self.head
            while fast.next!=None and fast.next.next!=None:
                fast=fast.next.next
                slow=slow.next
                newnode.next=slow.next
            slow.next=newnode
    def listsearch(self,key):
        curr=self.head
        while curr!=None:
            if curr.data==key:
                print("found")
                break
            curr=curr.next
        else:
            print("not found")
    def printlist(self):
        curr=self.head
        while(curr!=None):
            print(curr.data,"->",end=" ")
            curr=curr.next
        print("null")
l=linkedlist()
l.insertatbeg(1)
l.insertatbeg(2)
l.insertatbeg(3)
l.insertatend(4)
l.insertatend(5)
l.insertatend(6)
l.insertatend(7)
l.middle(10)
l.printlist()