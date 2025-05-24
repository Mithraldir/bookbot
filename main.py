from stats import count_words
from stats import character_count

def main():
    book_content = get_book_text("books/frankenstein.txt")
    print(book_content)
    word_count = count_words(book_content)
    print(f"{word_count} words found in the document")
    print(character_count(book_content))


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

    
main()