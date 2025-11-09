from stats import get_total_words

# Gets book text as string
def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    get_total_words(get_book_text("books/frankenstein.txt"))

main()