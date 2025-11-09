from stats import get_total_words
from stats import get_individual_word_count
from stats import return_report

# Gets book text as string
def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    sorted_list = return_report(get_individual_word_count(get_book_text("books/frankenstein.txt")))
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound 75767 total words\n--------- Character Count -------")
    for dict in sorted_list:
        char = dict["char"]
        if (char.isalpha() == False):
            pass
        else:
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")    
main()