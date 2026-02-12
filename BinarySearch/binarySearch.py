# Binary Search
# Sorted Array

def binary_search(arr, low, high, item):
    
    if low <= high:
        print("low = ",low,"high = ",high,end=' ')
        mid = (low + high) // 2
        print("mid value is ", arr[mid])
        
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binary_search(arr, low, mid-1, item)
        else:
            return binary_search(arr, mid+1, high, item)
    else:
        return -1
    

l = [12, 12, 33, 39,59, 66, 70, 76, 77, 95]
print(l)

print(binary_search(l, 0, len(l)-1, 95 ))


# without recursion
def binary_search2(arr, low, high, item):
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1