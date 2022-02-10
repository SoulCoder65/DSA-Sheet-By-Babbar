
def commanElements(A, B, C, n1, n2, n3):
    i=0
    j=0
    k=0
    ans_set=set()
    while i<n1 and j<n2 and k<n3:
        if A[i]==B[j]==C[k]:
            ans_set.add(A[i])
            i+=1
            j+=1
            k+=1
        elif A[i]<B[j]:
            i+=1
        elif B[j]<C[k]:

            j+=1
        else:
            k+=1
    ans_set=list(ans_set)
    ans_set.sort()
    return ans_set
n1 = 6
A = [1, 5, 10, 20, 40, 80]
n2 = 5
B = [6, 7, 20, 80, 100]
n3 = 8
C = [3, 4, 15, 20, 30, 70, 80, 120]
print(commanElements(A,B,C,n1,n2,n3))