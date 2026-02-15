def BubbleSort(arr):
    for i in range(len(arr)-1): # Outer loop to traverse through all elements
        flag = 0 # Flag to check if any swapping occurs in the inner loop
        for j in range(len(arr)-1-i): # Inner loop to compare adjacent elements
            if arr[j] > arr[j+1]: # If the current element is greater than the next element, swap them
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap the elements
                flag = 1 # Set the flag to 1 if a swap occurs
        if flag == 0: # If no swapping occurs in the inner loop, it means the array is already sorted, so we can
            break
            
    print(arr)

arr = [23, 12, 34, 11, 100, 56, 68]
BubbleSort(arr)