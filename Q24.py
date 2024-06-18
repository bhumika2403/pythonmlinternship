print("\t\t\t SIMPLE CALCULATOR \n\n")
print("1.addition\n2.subtraction\n3.multiplication\n4.division\n5.remainder")
num1=float(input("enter first number"))
num2=float(input("enter second number"))
choice=int(input("enter your choice(1-5):-"))
if(choice==1):
    print("sum is:-",num1,"+",num2,"is:-",(num1+num2))
elif(choice==2):
    print("subtacrtion is:-",num1,"-",num2,"is:-",(num1-num2))
elif(choice==3):
    print("multiplication is:-",num1,"*",num2,"is:-",(num1*num2))
elif(choice==4):
    print("division is:-",num1,"/",num2,"is:-",(num1/num2))
elif(choice==5):
    print("subtacrtion is:-",num1,"%",num2,"is:-",(num1%num2))
else:
    print("invalid choice")