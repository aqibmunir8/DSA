arr = [1,2,3,7,5,8]

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True



print(is_sorted(arr))





