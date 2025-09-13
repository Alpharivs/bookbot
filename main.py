import sys
from stats import (
    word_counter,
    character_counter,
    char_sorter,
)

# Open book.
def get_books_text(path):
    with open(path) as f:
        book_text = f.read()
    return book_text

# Display output.
def print_output(book_path, word_number, unique_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_number} total words")
    print("--------- Character Count -------")
    char_sorter(unique_chars)
    print("============= END ===============")

if __name__ == "__main__":
    # Argument check.
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_books_text(book_path)
    word_number = word_counter(book_text)
    unique_chars = character_counter(book_text)
    print_output(book_path, word_number, unique_chars)