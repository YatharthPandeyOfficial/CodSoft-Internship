num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number"))
operator=input("Choose Operation +,-,*,/")

if operator=="+":
    print("Sum is",num1+num2)

elif operator=="-":
    print("Difference is",num1-num2)

elif operator=="*":
    print("Product is",num1*num2)

elif operator=="/":
    print("Quotient is",num1/num2)

else:
    print("Invalid Operator")
    
