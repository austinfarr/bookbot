def get_word_count(text):
    words = text.split()
    return len(words) 

def get_char_count(text):
    chars = {}
    for i in text.lower():
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars

def sort_on(items):
    return items["num"]

def get_sorted_char_counts(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list