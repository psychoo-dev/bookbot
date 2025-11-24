import sys
from stats import count_words, get_number_of_characters, get_sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_characters = get_number_of_characters(book_text)
    sorted_list = get_sorted_list(num_characters)
    for item in sorted_list:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item["num"]}")
    print("============= END ===============")

main()