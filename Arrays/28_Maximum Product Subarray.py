def maxProduct(arr):
    if len(arr)<=1:
        return arr[0]
    max_val,min_val=arr[0],arr[0]
    result=max_val

    for i in range(1,len(arr)):
        curr=arr[i]
        temp_max=max(curr,max_val*curr,min_val*curr)
        min_val=min(curr,max_val*curr,min_val*curr)

        max_val=temp_max

        result=max(max_val,result)
    return result
arr=[6, -3, -10, 0, 2]

print(maxProduct(arr))