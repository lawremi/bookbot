from stats import count_words, count_each_letter, sort_table
import sys

def get_book_text(filepath: str):
    with (open(filepath)) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookpath = sys.argv[1]
    text = get_book_text(bookpath)
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print("Found " + str(count_words(text)) + " total words")
    letter_counts = sort_table(count_each_letter(text), reverse=True)
    print("--------- Character Count -------")
    for count in letter_counts:
        print(f"{count['char']}: {count['num']}")
    
if __name__ == "__main__":
    main()