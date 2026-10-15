# SET (UNORDERED MUTABLE ALLOW DUBLICATES)

numbers={45,67,89,90}
print(numbers)
names={"Ami","Adhi","kesavan"}
print(names)
empty_set=set()
empty_set={4,5,6}
print(empty_set)
nums={10,20,30,20,30,10}
print(nums)
print(len(nums))

list_1=[10,20,3,20,30,50,10]
unique_set=set(list_1)
print(unique_set)

nums_1={10,20,30}
nums_1.add(40)
print(nums_1)
nums_1.remove(50)
print(nums_1)
nums_1.remove(150)
print(nums_1)
nums_1.discard(40)
print(nums_1)
nums_1.discard(140)
print(nums_1)
for value in nums_1:
    print(value,end=" ")

a={1,2,3}
b={3,4,5}
print()
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

a={10,20}
b={10,20,30,40}
c={50,60}
print()
print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint(b))
print(b.isdisjoint(c))


