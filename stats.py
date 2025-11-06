
def count_words(text):
    words = []
    words = text.split()
    return len(words)

def count_per_char(text):
    to_lower_text = text.lower()

    set_of_words = set(to_lower_text)
    list_of_distinct_words = sorted(set_of_words)
    my_chars = dict.fromkeys(list_of_distinct_words, 0)

    for symbol in my_chars:
        for char in list(to_lower_text):
            
            if (symbol == char):
                my_chars[symbol] += 1
        
    return my_chars

def sort_by_count(letters_dict):
    list_of_dict = list()
    

    for k, v in letters_dict.items():
        temp = {'char': k, 'num': v}
        list_of_dict.append(temp)

    def sort_on(items):
        return items['num']
    
    list_of_dict.sort(reverse=True, key=sort_on)

    return list_of_dict