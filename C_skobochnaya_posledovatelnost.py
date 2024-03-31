# ID 110788697 / 28 мар 2024, 11:50:02

def is_correct_bracket_seq(massiv):

    stack: list = []
    
    for item in massiv:
        if massiv[0] in [')', '}', ']']:
            return False
        elif item in [')', '}', ']'] and '(' not in stack and '{' not in stack and '[' not in stack:
            return False
        elif item in ['(', '{', '[']:
            stack.append(item)
        elif item == ')' and stack[-1] == '(':
            stack.pop(-1)        
        elif item == '}' and stack[-1] == '{':
            stack.pop(-1)        
        elif item == ']' and stack[-1] == '[':
            stack.pop(-1)
        else: 
            stack.append(item) 
    
    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    code = input()
    print(is_correct_bracket_seq(code))
    