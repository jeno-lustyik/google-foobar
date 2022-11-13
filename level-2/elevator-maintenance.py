def solution(l):
    # Helper function for checking the numbers for sorting.
    def check(num1=str, num2=str):
        i, n = num1.split('.'), num2.split('.')
        # Compare the numbers in the two versions, iterating through the shorter one.
        m = min(len(i), len(n))
        for k in range(m):
            if int(i[k]) < int(n[k]):
                return 0
            elif int(i[k]) > int(n[k]):
                return 1
            else:
                continue
        # if the function didn't return, we'll compare their lengths.
        if len(i) < len(n):
            return 0
        else:
            return 1

    # Define a quicksort algorithm
    def sort(l):
        arr = l[::]
        if len(arr) <= 1:
            return arr

        left = [x for x in arr[1:] if check(x, arr[0]) == 0]
        right = [x for x in arr[1:] if check(x, arr[0]) == 1]
        return sort(left) + arr[0:1] + sort(right)

    return sort(l)
