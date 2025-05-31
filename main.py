from stats import count_words
from stats import character_count
from stats import sorter
import sys

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_content = get_book_text(sys.argv[1])
    #print(book_content)
    print(f"Analyzing book found at {sys.argv[1]}")
    word_count = count_words(book_content)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_counts = character_count(book_content)
    sorted_chars = sorter(char_counts)
    for entry in sorted_chars:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")
    
    


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

    
main()