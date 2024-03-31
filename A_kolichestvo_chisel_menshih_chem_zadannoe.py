# ID 110320984 / 22 мар 2024, 00:37:18

def count_nums(massiv):
    massiv2 = massiv[:]
    result = [0] * len(massiv)                  
    ind = 0
    for i in massiv:
        for j in massiv2:
            if i > j:
                result[ind] += 1
        ind +=1                
                                 
    result1 = [str(i) for i in result]
    return result1

if __name__ == '__main__':
    nums = [int(i) for i in input().split()]
    nums_result = count_nums(nums)   
    print(' '.join(nums_result))
    