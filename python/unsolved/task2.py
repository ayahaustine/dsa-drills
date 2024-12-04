"""
I need a function in Python that will take in an input word and create randomly
generated acronyms for it. The acronym should be based on words found in an already-defined valid_words.
The criteria uses the first letter of each character in the input word to select random words starting with
the same letter from the valid_words list.
"""

import random

def generate_acronym(input_word, valid_words):
    """
    Generate a random acronym based on the input word.

    Args:
        input_word (str): The input word to create the acronym for.
        valid_words (list): A list of valid words to use for the acronym.

    Returns:
        str: A randomly generated acronym.
    """
    # Ensure the input_word is uppercase to match first letters easily
    input_word = input_word.upper()
    # Filter the valid words by first letters for quick lookups
    word_dict = {}
    for word in valid_words:
        first_letter = word[0].upper()
        if first_letter not in word_dict:
            word_dict[first_letter] = []
        word_dict[first_letter].append(word)
    
    # Generate the acronym
    acronym = []
    for letter in input_word:
        if letter in word_dict and word_dict[letter]:
            
            acronym.append(random.choice(word_dict[letter]))
        else:
            
            acronym.append(letter)
    
    return " ".join(acronym)

valid_words = [
    "apple", "banana", "cherry", "date", "elephant", "fox",
    "grape", "honey", "iguana", "jelly", "kite", "lemon", "mango", 
    "nectarine", "orange", "pear", "quince", "raspberry", "strawberry",
    "tiger", "umbrella", "violet", "watermelon", "xylophone", "yogurt", "zebra"
]

input_word = "chat"
print(generate_acronym(input_word, valid_words))