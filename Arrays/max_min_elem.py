# Time Complexity:O(n)


# Maximum Value Program
def max_elem(arr,n):
    max_val=arr[0]
    for i in range(1,n):
        if arr[i]>max_val:
            max_val=arr[i]
    return max_val

# Min Value Program
def min_elem(arr,n):
    min_val=arr[0]
    for i in range(1,n):
        if arr[i]<min_val:
            min_val=arr[i]
    return min_val

arr=[12, 1234, 45, 67, 1]
n=len(arr)
print(max_elem(arr,n))
print(min_elem(arr,n))