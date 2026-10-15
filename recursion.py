# RECURSION - FUNCTION CALLING ITSELF

def greet(n):
    if n==0:
        return
    print("Hello amiadhi")
    greet(n-1)
greet(5)
print()

def printnum(a):
    if a==11:
        return
    print(a,end=" ")
    printnum(a+1)
printnum(1)

# RECURSION (FACTORIAL)

def factorial(num):
    if num==1:
        return 1
    return num*factorial(num-1)

num=int(input("Enter the number: "))
result=factorial(num)
print(result)