from stats import count_words, count_per_char, sort_by_count
import sys

def get_book_text(file):
    contents = ""
    with open(file) as f:
        contents = f.read()
    return contents
    
def main():
    if (len(sys.argv) != 2):
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    count = count_words(book_text)

    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {count} total words')
    print('--------- Character Count -------')

    count_of_all_symb = count_per_char(book_text)
    list_of_chars = sort_by_count(count_of_all_symb)

    for l in list_of_chars:
        if (l.get('char').isalpha()):
            print(f'{l.get('char')}: {l.get('num')}')



main()