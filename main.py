from stats import get_num_words
from stats import get_char_counts
from stats import split_char_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def print_info(path_to_file):
    text = get_book_text(path_to_file)
    word_count = get_num_words(text)
    char_counts = get_char_counts(text)
    list_of_dict = split_char_dict(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in list_of_dict:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book=sys.argv[1]
    print_info(path_to_book)


main()




