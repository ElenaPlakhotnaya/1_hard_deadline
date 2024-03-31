# ID 109625035 / 13 мар 2024, 21:42:19

def count_platforms(data: list[int], limit: int) -> int:
    """Считает сколько платформ потребуется для перевозки роботов."""
    data1 = sorted(data)
    left_pointer: int = 0
    right_pointer: int = len(data) - 1
    platforms: int = 0
    while left_pointer <= right_pointer:
        sum_weight = data1[left_pointer] + data1[right_pointer]
        platforms += 1
        right_pointer -= 1
        if sum_weight <= limit:
            left_pointer += 1
    return platforms


if __name__ == '__main__':
    robot_weights_input = [int(i) for i in input().split()]
    limit_input = int(input())
    print(count_platforms(robot_weights_input, limit_input))
    