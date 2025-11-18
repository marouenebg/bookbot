from stats import count_words,count_caracters,sort_list 
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    file_content = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    words_count = count_words(file_content)
    print (f"Found {words_count} total words")
    count_carac = count_caracters(file_content)
    print("--------- Character Count -------")
    listed_carac = sort_list(count_carac)
    for lis in listed_carac:
        if lis["char"].isalpha():
            print(f"{lis['char']}: {lis['num']}")
    print("============= END ===============")
main()
