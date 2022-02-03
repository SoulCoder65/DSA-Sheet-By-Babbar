def cyclicallyRotate(arr,n):
    temp=arr[n-1]
    for i in range(n-1,-1,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
    return arr



arr=[1,2,3,4,5,6]
n=len(arr)
print(cyclicallyRotate(arr,n))