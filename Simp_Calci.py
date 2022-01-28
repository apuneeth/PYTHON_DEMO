#getting inputs from user
a = int(input( "Enter 1st Number : "))
b = int(input( "Enter 2nd Number : "))

#getting the operator to be performed
c = input("Enter the Operation to be performed +, -, /, * : ")

while True:

    if c == "+": #performing addition
        s=a+b
        print("The Sum of ",a, "+",b, "is", s)
        break

    elif c == "-": #performing subtraction
        s=a-b
        print("The Difference of ",a, "-",b, "is", s)
        break

    elif c == "/": #performing division
        s=a/b
        print("The Quotient of ",a, "/",b, "is", s)
        break

    elif c == "*": #performing multiplication
        s=a*b
        print("The Product of ",a, "*",b, "is", s)
        break
    else:
        break