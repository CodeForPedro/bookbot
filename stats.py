# Counts number of words
def get_total_words(book_text):
    list_of_words = book_text.split()
    word_count = len(list_of_words)
    print(f"Found {word_count} total words")