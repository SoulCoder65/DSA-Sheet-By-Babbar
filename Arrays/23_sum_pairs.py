from collections import defaultdict
def sumPairs(arr,n,k):
    sum_val=0
    dict=defaultdict(lambda :0)

    for item in arr:
        val=k-item
        if val in dict.keys():
            sum_val+=dict[val]

        dict[item]+=1
    return sum_val

arr=[1, 1,1,1]
n=len(arr)
k=2
print(sumPairs(arr,n,k))