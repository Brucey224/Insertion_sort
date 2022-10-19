# Function to do insertion sort
def insertionSort(arr):
 
    # Traverse through indexes of array
    for i in range(1, len(arr)):
 
        ref = arr[i] # hold value of given index as reference

        j = i-1
        while j >=0 and ref < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = ref
 
 
# define array
arr = [1, 2, 8, 10, 51, 20, 8, 6, 4, 60]
insertionSort(arr)
lst = [] #empty list to store sorted elements
print("Sorted array is : ")
print(arr)
