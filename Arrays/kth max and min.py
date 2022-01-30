import heapq
# Time complexity of this solution is O(n + kLogn).
def k_max(arr,n,k):
    arr=[elem*-1 for elem in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -1*heapq.heappop(arr)

def k_min(arr,n,k):
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return heapq.heappop(arr)


arr=[ 12, 3, 5, 7, 19]
n=len(arr)
k=2
print(k_max(arr,n,k))
print(k_min(arr,n,k))