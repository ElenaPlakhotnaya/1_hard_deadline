# ID 110693190 / 27 мар 2024, 00:40:23

def podstroka(stroka):

    if not stroka:
        return 0
    max_length = 0
    left = 0
    right = 0
    podstr = set()

    while left < len(stroka) and right < len(stroka):
        if stroka[right] not in podstr:
            podstr.add(stroka[right])
            right += 1
            max_length = max(max_length, len(podstr))
        else:
            podstr.remove(stroka[left])
            left += 1
    return max_length


if __name__ == '__main__':
    code = input()
    print(podstroka(code))
    