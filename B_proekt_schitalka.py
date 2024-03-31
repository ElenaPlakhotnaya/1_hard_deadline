# ID 110098848 / 19 мар 2024, 11:42:48

def fun_count(x, y):
    if x == 1:
        return 1
    else:
        return (fun_count(x-1, y) + y - 1) % x + 1 
    

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    print(fun_count(n, k))
    