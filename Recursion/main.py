def reverseString(n):
    if n == '': return ''
    return reverseString(n[1:]) + n[0]

print(reverseString('hello'))