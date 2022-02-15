
def subArray(arr,n):
    dict_arr={}
    s=0
    for i in range(1,n):
        s+=arr[i]
        if s==0 or (s in dict_arr.keys()) or arr[i]==0:
            return "Yes"
        else:
            dict_arr[s]=1
    return "No"
arr=[1,2,3,4,5]
n=len(arr)

print(subArray(arr,n))