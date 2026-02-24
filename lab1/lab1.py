def sumOfTwo(nums: list, target: int) -> list[int] | None:
    '''находит индексы двух чисел в массиве, сумма которых равна target'''
    for i in range(len(nums) + 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

