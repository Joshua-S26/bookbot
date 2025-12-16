def get_number_words(text):
    count = 0
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(item): 
    return item["num"]

def sorted_chars(char_dict):
    list_of_dicts = []
    for ch, count in char_dict.items():
        list_of_dicts.append({"char": ch, "num": count})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts