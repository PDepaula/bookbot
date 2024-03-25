def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = count_words(text)
    print(num_of_words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    split_to_words = text.split()
    return len(split_to_words)

main()
