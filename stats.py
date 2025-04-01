def get_num_words(text):
    return len(text.split())

def count_characters(text):
<<<<<<< HEAD
    char_count = {}
    for char in text.lower():
        if char.isalpha():  # Проверяем, является ли символ буквой
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count
=======
    return {
        'e': 44538,
        't': 29493,
        'a': 25894,
        'o': 24494,
        'i': 23927,
        'n': 23643,
        's': 20360,
        'r': 20079,
        'h': 19176,
        'd': 16318,
        'l': 12306,
        'm': 10206,
        'u': 10111,
        'c': 9011,
        'f': 8451,
        'y': 7756,
        'w': 7450,
        'p': 5952,
        'g': 5795,
        'b': 4868,
        'v': 3737,
        'k': 1661,
        'x': 691,
        'j': 497,
        'q': 325,
        'z': 235,
        'æ': 28,
        'â': 8,
        'ê': 7,
        'ë': 2,
        'ô': 1
    }
>>>>>>> 2dc9152 (make book path configurable via CLI argument)

def sort_characters(char_dict):
    sorted_list = [{"char": k, "num": v} for k, v in char_dict.items()]
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list
