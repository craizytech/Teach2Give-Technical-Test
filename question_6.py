# Master Yoda, a renowned Jedi Master from the Star Wars universe, is known
# for his unique way of speaking. He often reverses the order of words in his
# sentences. For example, instead of saying "I am home" he might say "Home
# am I" Design a function that takes a sentence as input and returns a new
# sentence with the words reversed in the same order that Master Yoda would
# use.

def reverse_words(sentence):
    """This function takes a sentence,
    reverses the words in it and returns it
    
    Args:
        sentence (str): The string to be reversed
    
    Returns (str): The sentence in reversed order
    """
    new_list = sentence.split()
    return " ".join(new_list[::-1])

# Testing the function
print(reverse_words("My name is Eammon")) # Output: Eammon is name My