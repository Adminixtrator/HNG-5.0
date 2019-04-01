import math

while True:

    a = float(input("Please enter the first number \n"))
    c = str(input("Enter the operation to be carried out \n"))
    b = float(input("Please enter the second number \n"))

    if (c == "+" or c == "sum" or c == "add" or c == "plus" or c == "Plus" or c == "PLUS" or c == "addition" or c == "Addition" or c == "ADDITION"):
   
       sum = a + b
       print ("The sum is ",sum)
   
    elif (c == "-" or c == "difference" or c == "subtract" or c == "minus" or c == "Minus" or c == "MINUS" or c == "subtraction" or c == "Subtraction" or c == "SUBTRACTION"):
   
       diff = a - b
       print ("The difference is ",diff)
   
    elif (c == "/" or c == "" or c == "divide" or c == "division" or c == "Division" or c == "DIVISION" or c == "divide" or c == "Divide" or c == "DIVIDE"):
   
       div = a / b
       print ("The division is ",div)
   
    elif (c == "*" or c == "product" or c == "multiply" or c == "multiply" or c == "Multiply" or c == "MULTIPLY" or c == "multiplication" or c == "Multiplication" or c == "MULTIPLICATION"):
   
       multi = a * b
       print ("The product is ",multi)
     
    else:
       print ("Sorry, operation not found.")

    print('.'*70)

# &copy 2019 Aang Studios
# ADMINIXTRATOR CODES..

