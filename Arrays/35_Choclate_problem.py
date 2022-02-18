def findMinDiff(A, N, M):
    A.sort()
    min_val=float('inf')
    i=0
    while (i+M-1<N):
        d=A[i+M-1]-A[i]
        if d<min_val:
            min_val=d
        i+=1
    return min_val

A=[3, 4, 1, 9, 56, 7, 9, 12]
N=len(A)
M=5
print(findMinDiff(A,N,M))
