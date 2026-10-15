# if-else statement

#task1
mark=int(input("Enter the mark: "))
if mark>=90 and mark<=100:
    print("A")
elif mark>=75 and mark<=89:
    print("B")
elif mark>=60 and mark<=74:
    print("C")
elif mark>=40 and mark<=59:
    print("D")
else:
    print("FAIL")

#task2

num=int(input("Enter the number: "))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

#task3

num1=int(input("Enter the number1: "))
num2=int(input("Enter the number2: "))
num3=int(input("Enter the number3: "))
if num1>num2:
    if num1>num3:
        print("num1 is greater")
    else:
        print("num3 is greater")
else:
    if num2>num3:
        print("num2 is greater")
    else:
        print("num3 is greater")
#task4

amount=float(input("enter the purchase amount: "))
if amount>=5000:
    discount=amount*0.2
    print("discount amount:", discount)
    print("final amount:", amount-discount) 
elif amount>=2000 and amount<5000:
    discount=amount*0.1
    print("discount amount:", discount)
    print("final amount:", amount-discount)
elif amount<2000:
    print("no discount") 
else:
    print("invalid amount")  

#task5

temperature=float(input("Enter the temperature: "))
if temperature<20:
    print("cold")
elif temperature>=20 and temperature<30:
    print("pleasant")
elif temperature>=30 and temperature<40:
    print("hot")
else:
    print("very hot")

