from stats import get_num_words, count_characters

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    print(f"{get_num_words(text)} words found in the document")
    
    char_counts = count_characters(text)
    print("\nCharacter frequencies:")
    for char, count in sorted(char_counts.items()):
        print(f"'{char}': {count}")

if __name__ == "__main__":
    main()
