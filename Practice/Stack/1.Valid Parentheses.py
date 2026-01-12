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
def areBracketsProperlyMatched(code_snippet):
    # Write your code here
    left_nested_bracket = []
    for x in code_snippet:
        if x == "(" or x == "[" or x== "{":
            left_nested_bracket.append(x)
        else:
            if (x == ")" and left_nested_bracket.pop() != "(") or ( x == "]" and left_nested_bracket.pop() != "]") or ( x == "}" and left_nested_bracket.pop() != "}"):
                return False
            else:
                return True
    return True if len(left_nested_bracket) == 0 else False
print(areBracketsProperlyMatched("(}[]"))
print(validateParentheses("{[[(l))]]}"))