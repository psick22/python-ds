def merge_sort(lt, rt):
    if lt < rt:
        mid = (lt + rt) // 2
        merge_sort(lt, mid)
        merge_sort(mid + 1, rt)
        p1 = lt
        p2 = mid + 1
        temp = []
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                temp.append(arr[p1])
                p1 += 1
            else:
                temp.append(arr[p2])
                p2 += 1
        if p1 <= mid:
            temp = temp + arr[p1:mid + 1]
        if p2 <= rt:
            temp = temp + arr[p2:rt + 1]
        for i in range(len(temp)):
            arr[lt+i] = temp[i]


if __name__ == "__main__":
    arr = [23, 11, 45, 36, 15, 67, 33, 21]
    print("Before sort : ", end='')
    print(arr)
    merge_sort(0, 7)
    print()
    print("After sort : ", end='')
    print(arr)
