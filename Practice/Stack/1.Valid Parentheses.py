def validateParentheses(input):
    left_sign_stack = list()
    for x in input:
        if x == '{' or x == '(' or x == '[':
            left_sign_stack.append(x)
        elif x == '}' or x == ')' or x == ']':
            if len(left_sign_stack) > 0:
                if (x == '}' and left_sign_stack.pop() != '{') or (x == ']' and left_sign_stack.pop() != '[') or (x == ')' and left_sign_stack.pop() != '('):
                    return False
                else:
                    return True
            else:
                return False
    return True if len(left_sign_stack) == 0 else False
print(validateParentheses("{[[(l))]]}"))