inters_arr=[]
union_arr=[]

def union_and_intersection(arr1,arr2):
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]==arr2[j]:
            inters_arr.append(arr1[i])
            union_arr.append(arr1[i])

            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            union_arr.append(arr1[i])
            # union_arr.append(arr2[j])
            i+=1
        else:
            union_arr.append(arr1[i])
            # union_arr.append(arr2[j])
            j+=1


# arr1=[1, 3, 4, 5, 7]
# arr2=[2, 3, 5, 6]
arr1=[2, 5, 6]
arr2=[4, 6, 8, 10]
union_and_intersection(arr1,arr2)
print(union_arr)
print(inters_arr)