# ID 110359238 / 22 мар 2024, 17:00:24

def check_mountains(massiv):
    
    flag = False
    if len(massiv) < 3:
        return flag
    
    for i in range(len(massiv)-1):
        if massiv[i] == massiv[i+1]:
            return flag
    
    max_value = max(massiv)
    max_index_0 = massiv.index(max_value)
    max_index = (max_index_0)
    if max_index == len(massiv)-1:
        return flag
    
    left_numbers = list(massiv[0:max_index])
    right_numbers = list(massiv[max_index:])
    if len(right_numbers) > 1:
        list.reverse(right_numbers)
    
    
    
    if len(left_numbers) < 1 or len(right_numbers) < 1:
        flag = False
    
    else:
        left_numbers_test = left_numbers[:]
        left_numbers_test.sort()
        right_numbers_test = right_numbers[:]
        right_numbers_test.sort()
        if (left_numbers_test == left_numbers) and (right_numbers_test == right_numbers):
            flag = True
            
    return flag

if __name__ == '__main__':
    montain = [int(i) for i in input().split()]    
    print(check_mountains(montain))
    