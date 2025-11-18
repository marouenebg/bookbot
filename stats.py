def count_words(book):
    list_of_words = book.split()
    return len(list_of_words)

def count_caracters(book):
    count_caracters = {}
    for c in book:
        char_lower = c.lower()
        if char_lower not in count_caracters:
            count_caracters[char_lower] = 0
        count_caracters[char_lower] += 1
    return count_caracters

def sort_list(caract_dic):
    initial_list = []
    for c in caract_dic:
        interm_dic = {"char": c, "num": caract_dic[c]}
        initial_list.append(interm_dic)  # Fixed: interm_dic not interm_doc
    initial_list.sort(reverse=True, key=sort_on)
    return initial_list

def sort_on(item):  # Fixed: parameter name should match usage
    return item["num"]  # Fixed: item["num"] not items["num"]
