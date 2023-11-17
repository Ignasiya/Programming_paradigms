def binary_search(arr: [int], elem: int) -> int:
    start = 0
    end = len(arr) - 1

    def binary_search_recursive(arr: [int], elem: int, start: int, end: int) -> int:
        if start > end:
            return False

        mid = (start + end) // 2
        if elem == arr[mid]:
            return mid
        elif elem < arr[mid]:
            return binary_search_recursive(arr, elem, start, mid - 1)
        else:
            return binary_search_recursive(arr, elem, mid + 1, end)

    binary_search_recursive(arr, elem, start, end)


if __name__ == '__main__':
    arr = [1, 2, 7, 6, 11, 33, 45]
    number = int(input("Введите искомый элемент: "))
    result = binary_search(arr, number)
    if result == -1:
        print("Искомого элемента нет в массиве")
    else:
        print(f"Искомый элемент: {number} найден по индексу: {result}")
