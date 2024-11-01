"""
write a python function that takes a string 's'
and a dict that contains (animal name, animal voice) 
and returns the name of the animal whose voice is a 
sub sequence of s. if multiple animal voices exist print any.
"""

# possible solution 1

def is_subsequence(animal_voice, s):
    # Initialize pointers for both the animal_voice and the string s
    animal_index, s_index = 0, 0
    
    # Traverse through both strings
    while animal_index < len(animal_voice) and s_index < len(s):
        # If characters match, move to the next character in animal_voice
        if animal_voice[animal_index] == s[s_index]:
            animal_index += 1
        # Move to the next character in s
        s_index += 1
        
    # If we have gone through all characters in animal_voice, it's a subsequence
    return animal_index == len(animal_voice)

def find_animal_by_voice(s, animal_dict):
    for animal, voice in animal_dict.items():
        if is_subsequence(voice, s):
            return animal
    return None  # Return None if no matching animal is found

# Example usage:
animal_dict = {
    'dog': 'bark',
    'cat': 'meow',
    'cow': 'moo',
    'lion': 'roar',
}

s = "hbaroaokm"
animal_name = find_animal_by_voice(s, animal_dict)
print(animal_name)  # Output could be 'dog' or 'lion', based on subsequence found.


# probable solution 2

def is_subsequence(voice, s):
    s_idx = 0
    voice_idx = 0
    while s_idx < len(s) and voice_idx < len(voice):
        if voice[voice_idx] == s[s_idx]:
            voice_idx += 1
        s_idx += 1
    return voice_idx == len(voice)

def find_animal_with_voice(s, animals_dict):
    for animal, voice in animals_dict.items():
        if is_subsequence(voice, s):
            return animal
    return None

# Example usage:
animals_dict = {
    'dog': 'bark',
    'cat': 'meow',
    'cow': 'moo',
    'bird': 'tweet'
}

s = 'abcaaadefmbarkoaor'
print(find_animal_with_voice(s, animals_dict))  # Output could be 'dog' since "bark" is a subsequence of s