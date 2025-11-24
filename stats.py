def count_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def get_number_of_characters(book_text):
    char_dict = {}
    for i in book_text:
        i = i.lower()
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict

def get_sorted_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        small_dict = {"char": char, "num": count}
        char_list.append(small_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(item):
    return item["num"]
