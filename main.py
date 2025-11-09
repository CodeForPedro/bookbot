from stats import get_total_words
from stats import get_individual_word_count

# Gets book text as string
def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    get_total_words(get_book_text("books/frankenstein.txt"))
    print(get_individual_word_count((get_book_text("books/frankenstein.txt"))))
main()