n=int(input())
listone=[]
for i in range(n):
    data=int(input())
    listone.append(data)
left=0
right=len(listone)-1
while left<right:
    temp=listone[left]
    listone[left]=listone[right]
    listone[right]=temp
    left+=1
    right-=1
print(listone)