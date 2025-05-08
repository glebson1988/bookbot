from stats import word_count, print_content
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(path)} total words")
    print("--------- Character Count -------")
    print(print_content(path))
    print("============= END ===============")

main()
