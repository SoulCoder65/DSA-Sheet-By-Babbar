def largestsubSum(arr,n):
    curr_sum=0
    max_sum=arr[0]
    for i in range(n):
        curr_sum+=arr[i]
        if curr_sum>max_sum:
            max_sum=curr_sum
        if curr_sum<0:
            curr_sum=0

    return max_sum

arr=[-1,2,-3,-4]
n=len(arr)
print(largestsubSum(arr,n))