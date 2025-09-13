def word_counter(book_text):
    words = book_text.split()

    return len(words)

def character_counter(book_text):
    unique_words = {}
    
    for word in book_text:
        # Lowercase to prevent duplicates.
        word = word.lower()
        if word in unique_words:
            unique_words[word] += 1
        else:
            unique_words[word] = 1
    
    return unique_words

# Helper function for sorting list of dictionaries.
def sort_on(dictionary):
    return dictionary["num"]

def char_sorter(unique_words):
    sorted_list = []
    # Create array of lists with the keys char and num [{char: x, num: y},...]
    for ch in unique_words:
        if ch.isalpha():
            sorted_list.append({"char": ch, "num": unique_words[ch]})
    # Sort using the helper function.
    sorted_list.sort(reverse=True, key=sort_on)

    # output the values of the dictionaries in the list in the desired format.
    for i in sorted_list:
        print(f"{i['char']}: {i['num']}")
