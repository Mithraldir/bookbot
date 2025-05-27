from stats import count_words
from stats import character_count
from stats import sorter

def main():
    print("============ BOOKBOT ============")
    book_content = get_book_text("books/frankenstein.txt")
    #print(book_content)
    print("Analyzing book found at books/frankenstein.txt...")
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