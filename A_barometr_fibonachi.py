# ID 110055648 / 18 мар 2024, 18:59:39

index = int(input())


def listtt():
    spis: list[int] = [1, 1]
    n = 2
    while n < 33:
        new = spis[n -2] + spis[n -1]
        spis.append(new)
        n += 1
        
    return spis

list = listtt()

print(list[index])
