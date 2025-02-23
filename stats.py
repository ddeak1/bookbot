def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_counts(text):
    lowercase_text = text.lower()
    character_dict = {}
    for char in lowercase_text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def sort_on(character_counts):
    return character_counts["num"]