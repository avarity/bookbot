from stats import get_num_words

def get_book_text(path):
    """Читает файл, пропуская метаданные Gutenberg"""
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    start = text.find("*** START OF THE PROJECT GUTENBERG EBOOK") + 1
    end = text.find("*** END OF THE PROJECT GUTENBERG EBOOK")
    return text[start:end].strip()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()
