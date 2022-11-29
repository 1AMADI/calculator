import os
def add(n1,n2):
    return (n1+n2)
def subtract(n1,n2):
    return (n1-n2)
def multiply(n1,n2):
    return (n1*n2)
def divide(n1,n2):
    return (n1/n2)
operations={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
    }

def calculator():
    num1=int(input("enter the first number? \n"))
    for i in operations:
        print(i)
    prog_run=True
    while  prog_run:
        operator=input("pick any operation from above: \n")
        num2=int(input("enter the other number: \n"))
        os.system("cls")
        symbol=operations[operator]
        answer= symbol(num1,num2)
        print(f"{num1}{operator}{num2} ={answer}")
        state=input("wanna continue with the same number  \n" ).lower()
        os.system("cls")

        if state[0]=="y":
            num1=answer
        else:
            prog_run=False
            calculator()

calculator()