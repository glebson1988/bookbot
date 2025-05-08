def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(path_to_file):
    splitted_content = get_book_text(path_to_file).split()
    return len(splitted_content)

def counted_dict(path_to_file):
    content = get_book_text(path_to_file)
    char_counts = {}

    for char in content.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def unsorted_list(path_to_file):
    dictionary = counted_dict(path_to_file)
    list_of_dicts = []
    for char, amount in dictionary.items():
        inner_dict = {}
        inner_dict["char"] = char
        inner_dict["num"] = amount
        list_of_dicts.append(inner_dict)
    return list_of_dicts

def sort_on(dict):
    return dict["num"]

def sorted_list(path_to_file):
    u_list = unsorted_list(path_to_file)
    u_list.sort(reverse=True, key=sort_on)
    return u_list

def print_content(path_to_file):
    lst = sorted_list(path_to_file)
    for item in lst:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
