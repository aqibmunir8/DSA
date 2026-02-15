# Sorting

def is_sorted(arr): # check if the array is sorted
    for i in range(len(arr) - 1):
        if arr[i]>arr[i+1]:
            return False
    return True
    

# Monkey sort

import random
a=[1,2,4,3]
random.shuffle(a) # shuffle the array & make permanent random order
print(a)



import time

def monkey_sort(arr): # keep shuffling the array until it is sorted
    while not is_sorted(arr):
        time.sleep(1) # sleep for 1 second to slow down the process
        random.shuffle(arr)
        print(arr)
    print(arr)

monkey_sort(a)

# Time Complexity
# The time complexity of monkey sort is unbounded, as it can take an infinite amount of time to sort the array. In the worst case, it can take O((n+1)!) time, where n is the number of elements in the array. This is because there are n! possible permutations of the array, and each permutation has an equal probability of being the sorted order. Therefore, on average, it will take O((n+1)!) time to sort the array using monkey sort.