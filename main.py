def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(len(file_contents.split()))

def count_characters():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    counts_dict = {}
    for i in list(file_contents):        
        i = i.lower() 
        if i not in counts_dict:
            counts_dict[i] = 0
        counts_dict[i] += 1
    for key, value in counts_dict.items():
        print(key, value)
        

count_characters()