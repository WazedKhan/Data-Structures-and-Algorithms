def braces(A):
    stack = []
    for i in A:
        if i != ')':
            stack.append(i)
        else:
            count = 0
            while stack[-1] != '(':
                popped = stack.pop()
                if popped in "+-*/":
                    count += 1
            stack.pop()
            if count == 0:
                return 1
    return 0

A = "(a+(a+b))"
print(braces(A))