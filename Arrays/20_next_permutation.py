def reverse(array, i, j):
    # Make sure i is less than j
    if i > j:
        i, j = j, i
    # Reverse array[i:j+1]
    section = array[i:j+1]
    section.reverse()
    array[i:j+1] = section
def nextPermutation(arr,n):
    for i in range(n-2,-2,-1):
        if arr[i]<arr[i+1]:
            break

    if i<0:
        arr.reverse()

    else:
        for j in range(n - 1, i, -1):
            if arr[j] > arr[i]:
                break
        arr[i],arr[j]=arr[j],arr[i]
        reverse(arr,i+1,len(arr)-1)
    return arr

arr=[1,3,2]
n=len(arr)
print(nextPermutation(arr,n))