def arraySubset(a1,a2,n,m):
    dic={}
    for item in a1:
        dic[item]=1
    count=0
    for i in a2:
        if i in dic.keys():
            count+=1
    if count==m:
        return "Yes"
    return "No"


a1=[10, 5, 2, 23, 19]
a2=[19,5,3]
n=len(a1)
m=len(a2)
print(arraySubset(a1,a2,n,m))