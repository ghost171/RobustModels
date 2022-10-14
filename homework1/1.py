def right_parenthesis(text):
    is_right = []
    for ch in text:
        if ch == '(' or ch == '{' or ch == '[':
            is_right.append(ch)
        if ch == ')':
            if len(is_right) == 0:
                return "False"
            if is_right[len(is_right) - 1] != '(':
                return "False"
            else:
                is_right.pop()
        if ch == '}':
            if len(is_right) == 0:
                return "False"
            if is_right[len(is_right) - 1] != '{':
                return "False"
            else:
                is_right.pop()
        if ch == ']':
            if len(is_right) == 0:
                return "False"
            if is_right[len(is_right) - 1] != '[':
                return "False"
            else:
                is_right.pop()
    
    if len(is_right) == 0:
        return "True"
    else:
        return "False"


if __name__ == "__main__":
    text = input()
    print(right_parenthesis(text))