# Time Complexity : O(n)
# Iterative Way
# 1) Initialize start and end indexes as start = 0, end = n-1
# 2) In a loop, swap arr[start] with arr[end] and change start and end as follows :
# start = start +1, end = end – 1
def reverseArrayIterative(arr,n):
    start=0
    end=n-1
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr

# Recursive Way
# 2) Swap arr[start] with arr[end]
# 3) Recursively call reverse for rest of the array.
def reverseArrayRecursive(arr,start,end):
    if start>=end:
        return
    arr[start],arr[end]=arr[end],arr[start]
    reverseArrayRecursive(arr,start+1,end-1)



arr=[1,2,3,4,5,3,2,5,1231,2]
n=len(arr)
print(reverseArrayIterative(arr,n))
reverseArrayRecursive(arr,0,n-1)
print(arr)


