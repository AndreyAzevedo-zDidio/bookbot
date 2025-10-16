# python
from stats import get_num_words, get_num_characters
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text =  get_book_text(book_path)
    count = get_num_words(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    chars = get_num_characters(text)
    for item in chars:
        ch = item["char"]
        num = item["num"]
        print(f"{ch}: {num}")
    print("============= END ===============")
main()
