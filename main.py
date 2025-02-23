import sys
from stats import get_word_count, get_character_counts, sort_on

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"Found {word_count} total words")
    character_counts = get_character_counts(text)
    sorted_list = sorted_characters(character_counts)
    for value in sorted_list:
        if value["char"].isalpha():
            print(f"{value["char"]}: {value["num"]}")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


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


def sorted_characters(character_counts):
    sorted_list = []
    for char in character_counts:
        sorted_list.append({"char": char, "num": character_counts[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



main()