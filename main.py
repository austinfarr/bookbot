from stats import get_word_count
from stats import get_char_count
from stats import get_sorted_char_counts
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)

    chars = get_char_count(book_text)
    sorted_chars = get_sorted_char_counts(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


main()