def get_num_words(text):
    return len(text.strip().split())


def get_char_counts(text):
    char_dict = {}
    for char in text.lower():
        if char not in char_dict:
            char_dict[char]=1
        else:
            char_dict[char]+=1

    return char_dict


def split_char_dict(char_dict):
    list_of_dict =[]
    sorted_dict= dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dict)
    for key in sorted_dict:

        if key.isalpha():
            list_of_dict.append({"char": key, "num": sorted_dict[key]})

    return list_of_dict



