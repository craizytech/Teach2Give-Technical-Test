# Write a recursive function to calculate the factorial of a number

def factorial_num(num):
    """This function calculates the factorial of a number
    
    Args:
        num (int): This is the number to find the factorial for

    Returns: (int) The value of the number
    """
    if isinstance(num, int):
        if num < 0:
            return "Enter a positive integer"
        elif num == 0:
            return 1
        else:
            return num * factorial_num(num - 1)
    else:
        return "Enter a valid integer"

#Testing the function
print(factorial_num("me")) #output : "Enter a valid integer"
print(factorial_num(-5)) #output: "Enter a positive integer"
print(factorial_num(5)) #output: 120
    
    
