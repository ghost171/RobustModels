text = input()


is_right = []
for ch in text:
    if ch == '(' or ch == '{' or ch == '[' :
        is_right.append(ch)
    if ch == ')':
        if len(is_right) == 0:
            print("False")
            exit()
        if is_right[len(is_right) - 1] != '(':
            print("False")
            exit()
        else:
            is_right.pop()
    if ch == '}':
        if len(is_right) == 0:
            print("False")
            exit()
        if is_right[len(is_right) - 1] != '{':
            print("False")
            exit()
        else:
            is_right.pop()
    if ch == '[':
        if len(is_right) == 0:
            print("False")
            exit()
        if is_right[len(is_right) - 1] != ']':
            print("False")
            exit()
        else:
            is_right.pop()

if len(is_right) == 0:
    print("True")
else:
    print("False")