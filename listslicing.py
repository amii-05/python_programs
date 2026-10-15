# list slicing

arr=[10,20,30,40,50,60,70,80,90]    #list[start:end:step]
print(arr[1:5])  #20,30,40,50
print(arr[:3])   #10,20,30
print(arr[3:7])  #40,50,60,70
print(arr[::2])  #10,30,50,70,90    

arr1=[10,20,30,20,50]
print(30 in arr1)   #True
print(100 in arr1)  #False
print(arr1.index(20))  #1
print(arr1.count(20))  #2
print(arr1.count(100)) #0