def movezeros(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
             arr[j]=arr[i]
             j+=1
    while j<len(arr):
        arr[j]=0
        j+=1
    print(arr)

arr=[3,0,6,5,0,7,3,9,0,0,3,5]
movezeros(arr)