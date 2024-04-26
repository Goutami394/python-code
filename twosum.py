nums=[1,3,4,5,6,8]
target=12
def twosum(nums,target):
    a=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
             if nums[i]+nums[j]==target:
                a.append(i)
                a.append(j)
    return a
print(twosum(nums, target))