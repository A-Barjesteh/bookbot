from stats import get_word_count, get_character_count, sort_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        file_text = get_book_text(filepath)
        num_words = get_word_count(file_text)
        char_count = get_character_count(file_text)
        sorted_dict = sort_characters(char_count)
        print("============ BOOKBOT ============")
        print(f'Analyzing book found at {filepath}...')
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for x in sorted_dict:
            print(f'{x.get("char")}: {x.get("num")}')

main()