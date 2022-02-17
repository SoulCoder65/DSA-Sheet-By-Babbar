def find3Number(arr,n,X):
    arr.sort()
    for i in range(n):
        y=X-arr[i]
        low=i+1
        high=n-1
        while low<high:
            if arr[low]+arr[high]==y:
                return 1
            elif arr[low]+arr[high]>y:
                high-=1
            else:
                low+=1
    return 0

arr=[1 ,4, 45, 6, 10, 8]
n=len(arr)
print(find3Number(arr,n,13))