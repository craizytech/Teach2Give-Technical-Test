# Design a function that takes a string or sequence of characters as input and
# returns the character that appears most frequently.
# //Eg 11189 => '1'
# //hello => l

def most_appearing(string):
    """This method takes a string or sequence of characters as input
    and returns the character appearing most frequently
    
    Args:
        string (str): contains the characters
    
    Returns (str): The character that appears the most
    """
    strings_dict = {}
    for char in str(string):
        if char in strings_dict:
            strings_dict[char] += 1
        else:
            strings_dict[char] = 1
    
    maximum_count = 0
    most_frequent_char = None
    for char, count in strings_dict.items():
        if count > maximum_count:
            maximum_count = count
            most_frequent_char = char
    
    return most_frequent_char

# Testing the function
print(most_appearing('abbc')) # output = b
print(most_appearing(1234556)) # output = 5

    