"""SIMPLE TERMINAL BASED CALCULATOR"""
number_one = 0
number_two = 0
def ask_for_numbers():
    global number_two,number_one
    number_one = int(input("Enter first number: "))
    number_two = int(input("Enter Second number: "))

def choose_operand():
    print("""
          CHOOSE OPERATION:
          0 : Addition (+)
          1 : Subtraction (-)
          2 : Multipication (x)
          3 : Division (/)
          4 : Modulus
          """)
    operation_chosen = int(input("Choose one from the above choices: "))
    
    if operation_chosen < 5 and operation_chosen >= 0:
        if operation_chosen == 0:
            return number_one + number_two
        elif operation_chosen == 1:
            return number_one - number_two
        elif operation_chosen == 2:
            return number_two * number_one
        elif operation_chosen == 3:
            try:
                return number_one / number_two
            except ZeroDivisionError as zde:
                return f"error: {zde}"
        elif operation_chosen == 4:
            return number_one % number_two

ask_for_numbers()
print(choose_operand())


