while True:
    print("Simple Calculator")
    print(" 1:Addition")
    print(" 2:Subtraction")
    print(" 3:Multiplication")
    print(" 4:Division ")
    print(" 5:Exit")
    opr=float(input("Select a operation: "))
    if opr==1:
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
        print(num1,"+",num2,"=",num1+num2)

    elif opr==2:
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
        print(num1,"-",num2,"=",num1-num2)

    elif opr==3:
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
        print(num1,"*",num2,"=",num1*num2)

    elif opr==4:
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
        if num2!=0:
            print(num1,"/",num2,"=",num1/num2)
        else:
            print("Error! Division by zero is not allowed.")
    elif opr==5:
        print("Exiting Calculator")
        break
    else:
        print("Invalid input")
