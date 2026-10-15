#LAMBDA FUNCTION - IT IS A SMALL ANONYMOUS FUNCTION CONTAINING A SINGLE EXPRESSION

#SYNTAX - lambda arguments:expression

square=lambda n:n*n
n=int(input())
result=square(n)
print(result)

addition=lambda a,b:a+b
total=addition(4,5)
print(total)

cube=lambda n:n*n*n
n=int(input("Enter the number: "))
result=cube(n)
print(result)


