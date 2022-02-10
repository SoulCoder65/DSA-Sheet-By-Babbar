def countInversion(arr):
    count = 0

    if len(arr)>1:
        mid=len(arr)//2
        left_arr=arr[:mid]
        right_arr=arr[mid:]
        count+=countInversion(left_arr)
        count+=countInversion(right_arr)
        i=0
        j=0
        k=0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
                k+=1
            else:
                count+=(mid-i)
                arr[k]=right_arr[j]
                j+=1
                k+=1
        while len(left_arr)>i:
            arr[k]=left_arr[i]
            i+=1
            k+=1
        while len(right_arr)>j:
            arr[k]=right_arr[j]
            j+=1
            k+=1
    return count


arr=[1, 20, 6, 4, 5]
print(countInversion(arr))

