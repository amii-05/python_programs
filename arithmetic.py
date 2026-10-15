name=input("Enter student name: ")
tamil=int(input("Enter tamil mark: "))
english=int(input("Enter english mark: "))
maths=int(input("Enter maths mark: "))
print("Student Name:", name)
total=tamil+english+maths
print("Total Marks:", total)
print("Average Marks:", total/3)

#lesserthan or graterthan

mark=int(input("Enter mark: ") )
print(mark >=40)

#task

balance=float(input("Enter balance: "))
deposit_amount=float(input("Enter deposit amount: " ))
expense_amount=float(input("Enter expense amount: " ))
balance += deposit_amount
balance -= expense_amount
print("final balance:", balance)