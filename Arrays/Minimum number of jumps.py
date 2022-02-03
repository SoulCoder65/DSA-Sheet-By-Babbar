def minJump(arr,n):
    min_jump=0
    curr_pos=0
    index=0
    while arr[index]<n:
        # print(curr_pos)
        index+=arr[curr_pos]
        curr_pos=arr[index]
        min_jump+=1
        print(min_jump)


arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n=len(arr)
print(minJump(arr,n))