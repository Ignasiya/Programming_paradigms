def sort_list_imperative(nums: list[int]):
    if len(nums) <= 1:
        return list
    for i in range(1, len(nums)):
        k = nums[i]
        j = i - 1
        while j >= 0 and nums[j] < k:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = k


def sort_list_declarative(nums: list[int]):
    if len(nums) <= 1:
        return list
    else:
        return nums.sort(reverse=True)


if __name__ == '__main__':
    numbers_1 = [9, 5, 1, 3, 2, 4, 6, 7, 8]
    sort_list_declarative(numbers_1)
    print(numbers_1)

    numbers_2 = [9, 5, 1, 3, 2, 4, 6, 7, 8]
    sort_list_imperative(numbers_2)
    print(numbers_2)
