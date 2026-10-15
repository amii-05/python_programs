num=int(input("enter the num: "))
digits=0
temp=num
temp1=num
while num!=0:
    rem=num%10
    digits+=1
    num=num//10
sums=0
while temp!=0:
    rem=temp%10
    sums+=rem**digits
    temp=temp//10
if sums==temp1:
    print(temp1,"is armstrong number")
else:
    print(temp1,"is not armstrong number")
