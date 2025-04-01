from stats import get_num_words, count_characters, sort_characters

def get_book_text(path):

    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    start = text.find("*** START OF THE PROJECT GUTENBERG EBOOK") + 1
    end = text.find("*** END OF THE PROJECT GUTENBERG EBOOK")
    return text[start:end].strip()

def print_report(book_path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    word_count = get_num_words(text)
    char_counts = count_characters(text)
    sorted_chars = sort_characters(char_counts)
    
    print_report(book_path, word_count, sorted_chars)

if __name__ == "__main__":
    main()
