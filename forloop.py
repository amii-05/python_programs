
#FOR LOOP

for i in range(10):
    print("AMIADHI")

for i in range(1,11):
    print(i)

for i in range(1,101,2):
    print(i,end=" ")
print()

for i in range(100,0,-1):
    print(i,end=" ")

#TASK1

num=int(input("enter the number:"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)

#TASK2

num1=int(input("enter the num1: "))
num2=int(input("enter the num2: "))
total=0
for i in range(num1,num2+1):
    if i%2==0:
        total=total+i
print(total)

#TASK3

num=int(input("enter the num: "))
for i in range(1,11):
    print(num," * ", i ," = ",num*i)

 #TASK4
    
num=int(input("enter the num: "))
fact=1
for i in range(num,0,-1):
    fact=fact*i
    print(i,end= " ")
    if i!=1:
        print("*", end=" ")
print(" = ", fact)