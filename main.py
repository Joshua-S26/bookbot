def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_number_words(text)
    print(f"Found {num_words} total words")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_words(text):
    count = 0
    words = text.split()
    return len(words)
main()
