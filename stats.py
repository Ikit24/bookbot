import sys

def sort_on(dict):
    return dict["num"]

def get_num_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    print(f"{len(file_contents.split())} words found in the document")
 
    counts_dict = {}
    for i in list(file_contents):
        if i.isalpha():
            i = i.lower()
            if i not in counts_dict:
                counts_dict[i] = 1
            else:
                counts_dict[i] += 1

    char_list = []
    for char, count in counts_dict.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=sort_on)

    for item in char_list:
        print(f"{item['char']}: {item['num']}")
