# ID 109049490 / 7 мар 2024, 11:36:33

from typing import List

len_num = input()
massiv1 = input().split()
massiv2: List[int] = []
massiv3: List[str] = []


def check_massiv(massiv_1: List[int], massiv_2: List[int], massiv_3: List[str]) -> List[int]:
    for item in massiv_1:
        if item not in massiv_2 and item != ' ':
            list.append(massiv_2, item)
        elif item in massiv_2:
            list.append(massiv_3, '_')
        else:
            continue
            
    return massiv_2


y = check_massiv(massiv1, massiv2, massiv3)


list.extend(massiv2, massiv3)

print(' '.join(massiv2))
