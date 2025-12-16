from stats import get_number_words, get_chars_dict, sorted_chars
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])

    num_words = get_number_words(text)
    num_char = get_chars_dict(text)
    sorted_list = sorted_chars(num_char)

    # print(f"Found {num_words} total words")
    # print("Character count:", num_char)
    print(f'''
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
          ''')
    for item in sorted_list:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")

def get_book_text(text):
    with open(text) as f:
        return f.read()

main()

