def kadaneAlgorithm(arr,n):
    curr_sum=0
    max_sum=0
    for i in range(n):
        curr_sum+=arr[i]
        if curr_sum>max_sum:
            max_sum=curr_sum
        elif curr_sum<0:
            curr_sum=0
    return max_sum

arr=[1,2,3,-2,5]
n=len(arr)
print(kadaneAlgorithm(arr,n))