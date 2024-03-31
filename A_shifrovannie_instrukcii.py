# ID 110217089 / 20 мар 2024, 17:53:14

def encrypted_instruction(code):
    stack = []
    help_num = 0
    help_str = ''

    for i in code:
        if i.isdigit():
            help_num = help_num * 10 + int(i)
        elif i == '[':
            stack.append((help_num, help_str))
            help_num = 0
            help_str = ''
        elif i == ']':
            num, str = stack.pop()
            help_str = str + help_str * num
        else:
            help_str += i

    return help_str

if __name__ == '__main__':
    code = input()
    print(encrypted_instruction(code))
    