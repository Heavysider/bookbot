from stats import number_of_words, number_of_each_character, sorted_characters_counts
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        text = file.read()
    return text

def main():
    # filepath = 'books/frankenstein.txt'
    # Check if the user provided a file path as a command line argument
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = number_of_words(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for pair in sorted_characters_counts(number_of_each_character(book_text)):
        print(f"{pair[0]}: {pair[1]}")
    print("============= END ===============")

main()
