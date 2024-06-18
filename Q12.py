n=int(input("enter the number to find its sum:-"))
sum=0
rem=0
temp=n
while(temp>0):
    rem=temp%10
    sum=sum+rem
    temp//=10
print("sum of digits",sum)