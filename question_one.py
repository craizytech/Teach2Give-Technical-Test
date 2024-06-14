# Design a function that reverses the digits of an integer. For example, 50
# should become 5 and -12 should become -21.

def reverse_int(num):
    """This method reverses the digits of an integer
    
    Args:
        num (int): The number to be revised
    
    Returns: (int) The reversed number
    """
    if num < 0:
        num = str(num * -1)
        return int(num[::-1])* -1
    elif num > 0:
        num = str(num)
        return int(num[::-1])
    else:
        return 0
    
#Testing the function 
print(reverse_int(50)) # should print 5
print(reverse_int(-12)) # should print -21
print(reverse_int(36)) # should print 63