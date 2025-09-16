def get_word_count(text):
    num_words = text.split()
    word_count = len(num_words)
    return word_count

def get_character_count(text):
    characters = {}
    for t in text.lower():
        if t in characters:
            characters[t] += 1
        else:
            characters[t] = 1
    return characters

def sorter(sort_list):
    return sort_list["num"]

def sort_characters(characters):
    sort_characters = []
    for key, value in characters.items():
        if key.isalpha():
            new_dict = {"char": key, "num": value}
            sort_characters.append(new_dict)
    print(sort_characters)
    sort_characters.sort(reverse=True, key=sorter)
    return sort_characters