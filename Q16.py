n=int(input("enter the number  :-"))
d=int(input("enter the digit of which we find the freq"))
rem=0
temp=n
count=0
while(temp>0):
           rem=temp%10
           if(rem==d):     
             count+=1
           temp//=10
print("the freq of ",d,"is",count)





















