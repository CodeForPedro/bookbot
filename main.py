import sys

from stats import get_total_words
from stats import get_individual_word_count
from stats import return_report

# Gets book text as string
def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    # Gets path to book
    user_input = sys.argv
    if len(user_input) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = user_input[1]

    # Gets sorted list from letter count dict
    sorted_list = return_report(get_individual_word_count(get_book_text(path_to_book)))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    get_total_words(get_book_text(path_to_book))
    print("--------- Character Count -------")

    # Formats and prints sorted list data
    for dict in sorted_list:
        char = dict["char"]
        if (char.isalpha() == False):
            pass
        else:
            print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")

main()