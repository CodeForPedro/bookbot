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

# Print report
def return_report(char_dict):
    dict_list = []
    for key in char_dict:
        my_dict = {}
        my_dict["char"] = key
        my_dict["num"] = char_dict[key]
        dict_list.append(my_dict)

    def sort_on(items):
        return items["num"]

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list