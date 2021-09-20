# linear Search

list_ = [13, 9, 8, 4, 2, 1]
num = 10

def find_num(list_, num):
    for i in range(len(list_)):
        if list_[i] == num:
            return i
    return -1

print(find_num(list_, num))