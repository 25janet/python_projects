
def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 == 0:
       return "Error!not divisible by zero.."
    else:
        return num1/num2
print("Welcome to the calculator")
while True:
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Choose the operator (+,-,*,/): ")
        num2 = float(input("Enter the second number: "))
        match operator:
            case '+':
                result = add(num1, num2)
            case '-':
                result = subtract(num1,num2)
            case '*':
                result = multiply(num1,num2)
            case '/':

                result= divide(num1,num2)
            case _:
                    
                    print("invalid operator")
                    continue
        print(f"Result: {result}")
    except ValueError:
          print("Invalid numbers.please enter numbers")
    again = input("Do you want to perform calculations.(yes/no)").strip().lower()
    if again != "yes":
        print("Goodbye!")
        break
        
    

