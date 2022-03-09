def minSwap (arr, n, k) :
    count=0
    for i in range(n):
        if arr[i]<= k:
            count+=1
    bad=0
    for i in range(count):
        if arr[i]>k:
            bad+=1

    i=0
    j=count
    ans=bad
    while j<n:
        if arr[i]>k:
           bad-=1
        if arr[j]>k:
            bad+=1
        ans=min(bad,ans)
        i+=1
        j+=1
    return ans
arr=[2, 1, 5, 6, 3]
n=len(arr)
k=3
print(minSwap(arr,n,k))