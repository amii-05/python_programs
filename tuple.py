# tuple ordered , immutable allow dublicates

numbers=(10,20,30,40)
print(numbers)
print(type(numbers))
arr=(5,)
print(type(arr))
print(numbers[2])
print(numbers[-1])
print(numbers[1:4])

for values in numbers:
    print(values,end=" ")
print()
arr2=(10,20,30,20)
print(arr2.count(20))
print(arr2.index(30))
print(len(arr2))
print(min(arr2))
print(max(arr2))
print(sum(arr2))

marks=(85,35,60,28,90,40)
pass_count=fail_count=0
for i in marks:
    if i>=40:
        pass_count+=1
    else:
        fail_count+=1
print("passed student: ", pass_count)
print("failed student: ", fail_count)
