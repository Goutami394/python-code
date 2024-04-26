l=[1,1,2,2,3,3,3]
room=[]
for i in l:
    if i not in room:
        room.append(i)
print(room)