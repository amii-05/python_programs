#sorting a list

arr2=[10,30,50,200,40]
arr2.sort()   #ascending order
print(arr2)
arr2.sort(reverse=True)  #descending order
print(arr2)

arr3=[10,40,50,200,40]
arr3.reverse()   #reverse the list
print(arr3)

arr4=[10,40,50,200,40]
print(len(arr4))   #length of the list
print(sum(arr4))   #sum of the list
print(max(arr4))   #maximum value in the list
print(min(arr4))   #minimum value in the list   

#task

nums=[]
pos=neg=zero=0
n=int(input("enter the number of n: "))
for i in range(n):
    value=int(input("enter the values: "))
    nums.append(value)
for value in nums:
    if value < 0:
        neg+=1
    elif value > 0:
        pos+=1
    else:
        zero+=1
print("List values: ", nums)
print("pos count: ", pos)
print("Neg count: ", neg)
print("zeros count: ", zero)