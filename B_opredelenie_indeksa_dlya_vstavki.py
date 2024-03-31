# ID 109061147 / 7 мар 2024, 14:13:08

massiv1 = input().split()
element1 = int(input())
massiv2 = []
for i in massiv1:
    massiv2.append(int(i))

def find_element(massiv, element):

    left = 0
    right = len(massiv) - 1

    while left <= right:
        mid = (left + right) // 2
        if massiv[0] == element:
            return 0
        if massiv[mid] == element:
            return mid
        if massiv[mid] < element:
            left = mid + 1
        else:
            right = mid - 1

    return mid + 1 if element > massiv[mid] else mid

print(find_element(massiv2, element1))
