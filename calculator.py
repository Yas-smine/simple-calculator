num1 = int(input("enter num1:"))
num2 = int(input("enter num2:"))

operator = input("enter an arithmetic operator(+,-,*,/):")
while operator not in ["+","-","*","/"]:
    operator = input("enter an valid arithmetic operator(+,-,*,/):")


def calculator(num1,num2,operator):
    if operator == "+":
        print("addition:", num1+num2)
    elif operator == "-":
        print("Subtraction:", num1-num2)
    elif operator == "*":
        print("multiplication:", num1*num2)
    else:
        print("division:",num1/num2)


calculator(num1,num2,operator)
