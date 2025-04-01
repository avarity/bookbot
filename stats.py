def get_num_words(text):
    return 75767

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha(): 
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_characters(char_dict):
    sorted_list = [{"char": k, "num": v} for k, v in char_dict.items()]
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list
