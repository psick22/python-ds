def quick_sort(lt, rt):
    if lt < rt:
        pos = lt
        pivot = arr[rt]
        for i in range(lt, rt):
            if arr[i] <= pivot:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1
        arr[rt], arr[pos] = arr[pos], arr[rt]
        quick_sort(lt, pos - 1)
        quick_sort(pos + 1, rt)


if __name__ == "__main__":
    arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
    print("Before sort : ", end='')
    print(arr)
    quick_sort(0, 9)
    print()
    print("After sort : ", end='')
    print(arr)
