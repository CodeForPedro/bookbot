# Counts number of words
def get_total_words(book_text):
    list_of_words = book_text.split()
    word_count = len(list_of_words)
    print(f"Found {word_count} total words")

# Counts amount of each letter
def get_individual_word_count(book_text):
    char_dict = {}
    lowercase_text = book_text.lower()
    for character in lowercase_text:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict