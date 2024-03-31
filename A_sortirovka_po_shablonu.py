# ID 110322123 / 22 мар 2024, 01:45:08

def sort_instr(massiv1, massiv2):

    help_massiv = []
    help_massiv1 = []
    for j in massiv2:
        for i in massiv1:
            if i == j:
                help_massiv.append(j)
            else:
                continue

    help_massiv1 = [item for item in massiv1 if item not in massiv2]

    help_massiv1.sort()

    list.extend(help_massiv, help_massiv1)
    return(help_massiv)

if __name__ == '__main__':
    m = int(input())
    need_sort = [int(i) for i in input().split()]
    n = int(input())
    instr_sort = [int(i) for i in input().split()]
    result = sort_instr(need_sort, instr_sort)
    result1 = [str(i) for i in result]
    print(' '.join(result1))
    