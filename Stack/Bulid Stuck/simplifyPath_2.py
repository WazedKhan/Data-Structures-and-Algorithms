path = "/home/../../temp//./"

def simplifyPath(path: str):
    res = []
    for pattern in path.split('/'):
        if pattern not in ['', '.', '..']:
            res.append(pattern)
        if pattern == '..' and res:
            res.pop()
    return '/'+'/'.join(res)

print(simplifyPath(path))