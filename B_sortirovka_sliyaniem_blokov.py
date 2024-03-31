# ID 110767212 / 27 мар 2024, 22:49:46

def check(massiv):

    spis = []
    count = 1
    ind_0 = massiv.index(0)    
    spis1 = massiv[0:ind_0 + 1]
    
    for i in massiv:
        if i not in spis1:
            spis.append(i) 

    for i in spis:
        if max(spis1) == len(spis1) - 1:
            count += 1
            spis1.append(i)
        else:
            spis1.append(i)

    return count
    
if __name__ == '__main__':
    n = int(input())
    code = [int(i) for i in input().split()] 
    print(check(code))
