# Design a function that takes a list of integers as input. The function should
# return True if the list contains two consecutive threes (3 next to a 3) anywhere
# within the list. Otherwise, it should return False. For example, the function
# should return True for [1, 3, 3] and False for [1, 3, 1, 3].

def consecutive_threes(num_list):
    """This function checks for consecutive numbers in the list
    
    Args:
        num_list (list): The list containing the numbers
    
    Returns (Boolean): True/False
    """
    for i in range(len(num_list) - 1):
        if num_list[i] == 3 and num_list[i + 1] == 3:
            return True
    return False

# Testing the function
print(consecutive_threes([1, 3, 3])) # Output: True
print(consecutive_threes([1, 3, 1, 3])) # Output: False
