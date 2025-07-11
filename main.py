import sys
from stats import get_num_words

def main():
    if len(sys.argv) < 2:
        print("Error sys.argv needs to arguments. Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(f"--- Begin report of {sys.argv[1]} ---")
    print()
    get_num_words(sys.argv[1])
    print()
    print("--- End report ---")


if __name__ == '__main__':
    main()
