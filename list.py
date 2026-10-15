#LIST - ordered, mutable collection of elements and allows duplicate values

numbers=[10,20,30,40,20]
names=["ami,adhi","abi","hari","guru","aku"]
mixed=[10,"ami",20.5]
print(numbers)
print(names)
print(mixed)
print(numbers[0])
print(numbers[2])
print(numbers[1])
print(names[1])
print(mixed[2])
print(numbers[-1])
print(names[-2])
numbers[2]=3000
print(numbers)

num=[]
n=int(input("enter the number of elements: "))
for i in range(n):
    value=int(input("enter the element: "))
    num.append(value)
print(num)
