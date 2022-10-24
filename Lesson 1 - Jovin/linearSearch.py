list_ = [13, 9, 8, 4, 2, 1]

def linearSearch(targer, list_):
    # function to find targer values index number 
    for index, value in enumerate(list_):
        if targer == value:
            return index

    return -1

print(linearSearch(1, list_))