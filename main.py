from stats import get_number_words, get_chars_dict, sorted_chars

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_number_words(text)
    num_char = get_chars_dict(text)
    sorted_list = sorted_chars(num_char)

    # print(f"Found {num_words} total words")
    # print("Character count:", num_char)
    print(f'''
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
          ''')
    for item in sorted_list:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

