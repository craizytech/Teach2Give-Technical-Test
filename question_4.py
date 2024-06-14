# Design a function that determines whether a given string is a pangram. A
# pangram is a sentence or phrase containing every letter of the alphabet at
# least once. Punctuation and case are typically ignored. For example, the
# string "The quick brown fox jumps over the lazy dog" is a pangram, while
# "Hello, world!" is not.

def is_panagram(string):
    """This function checks wether the string is a pangram
    
    Args:
        string (str): This is the string to be checked
    
    Returns (boolean): True or False
    """
    for i in range(97, 123):
        if chr(i) not in string:
            return False
    return True

# Testing on the function
print(is_panagram('abcdefghijklmnopqrstuvwxyz')) #output: True
print(is_panagram('asdfdffre')) #output: False
print(is_panagram('jnkdsnvknidjsinjsdvnivide')) #output: False