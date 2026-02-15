    # def selection_sort(arr):
        
    #     for i in range(len(arr) - 1):
    #         min = i
    #         for j in range(i+1, len(arr)):
    #             if arr[j] < arr[min]:
    #                 min = j
    #         arr[i], arr[min] = arr[min], arr[i]

    #     print(arr)

    # # Example usage
    # arr = [64, 25, 12, 22, 11]
    # selection_sort(arr)



def selection_sort(arr):
    
    for i in range(len(arr) - 1):
        print(i+1, "pass", end=" ")
        min = i
        print("current min is ", arr[min])
        for j in range(i+1, len(arr)):
            print("Current item under observation", arr[j])
            if arr[j] < arr[min]:
                print("Current item is less then min")
                min = j
                print("Now min has become", arr[min])
        arr[i], arr[min] = arr[min], arr[i]
        print("*"*50)

    print(arr)
    

arr = [64, 25, 12, 22, 11]
print(arr)
selection_sort(arr)