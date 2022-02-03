def minimizeHeight(arr,n,k):
    arr.sort()
    ans=arr[n-1]-arr[0]
    smallest=arr[0]+k
    largest=arr[n-1]-k
    min_val=0
    max_val=0
    for i in range(n-1):
        min_val=min(smallest,arr[i+1]-k)
        max_val=max(largest,arr[i]+k)
        if min_val<0:
            continue
        ans=min(ans,max_val-min_val)
    return ans
arr=[3, 9, 12, 16, 20]
k=3
n=len(arr)
print(minimizeHeight(arr,n,k))