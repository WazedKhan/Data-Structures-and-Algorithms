root = [1,2,5,3,4,'null',6]
root.remove('null')
root.sort()
tree = []


for i in range(1, len(root)+1):
    tree.append(root[i-1])
    if root[i-1] != root[-1]:
        tree.append('null')
    else:
        break

print(tree)