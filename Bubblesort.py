listone=[5,1,4,2,8,5,1,4,9,3,0,2,6,8,7,98,200]
for i in range(len(listone)-1):
    for j in range(len(listone)-1-i):
        if listone[j]>listone[j+1]:
            temp=listone[j]
            listone[j]=listone[j+1]
            listone[j+1]=temp
print(listone)