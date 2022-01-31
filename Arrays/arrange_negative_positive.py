# METHOD 1
# Time complexity: O(N)
# Auxiliary Space: O(1)
def rearrange(arr,n):
    j=0
    for i in range(n):
        if arr[i]<0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr

# METHOD 2

'''
Time complexity: O(N) 
Auxiliary Space: O(1)

Two Pointer Approach: The idea is to solve this problem with constant space and linear time is by using a two-pointer or two-variable approach where we simply take two variables like left and right which hold the 0 and N-1 indexes. Just need to check that :

Check If the left and right pointer elements are negative then simply increment the left pointer.
Otherwise, if the left element is positive and the right element is negative then simply swap the elements, and simultaneously increment and decrement the left and right pointers.
Else if the left element is positive and the right element is also positive then simply decrement the right pointer.
Repeat the above 3 steps until the left pointer ≤ right pointer.
'''
def rearrange_two_pointers(arr,n):
    l=0
    r=n-1
    while l<r:
        if arr[l]>0 and arr[r]<0:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
        elif arr[l]<0 and arr[r]<0:
            l+=1
        else:

            r-=1
    return arr

arr=[-1, 2, -3, 4, 5, 6, -7, 8, 9]
n=len(arr)
print(rearrange_two_pointers(arr,n))