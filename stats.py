def count_words(book_content):
    num_words = book_content.split()
    return len(num_words)

def character_count(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorter(char_count):
    list = []
    for char, count in char_count.items():
        final = {"char" : char, "num" : count }
        list.append(final)
    list.sort(key=lambda x: x["num"], reverse=True)
    return list