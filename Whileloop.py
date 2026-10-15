num=int(input("enter the num: "))
digit=0
total=0
while num!=0:
    rem=num%10
    digit+=1
    total+=rem
    num=num//10 
print("number of digit:", digit)
print("sum of digits: ", total)


num=int(input("enter the num: "))
while not (num>=0 and num<=9):
    sums=0
    while num!=0:
        rem=num%10
        sums+=rem
        num=num//10
    num=sums
else:
    print(num)
