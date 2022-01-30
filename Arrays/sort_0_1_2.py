def sortArray(arr,n):
    count_0=0
    count_1=0
    count_2=0
    for item in arr:
        if item==0:
            count_0+=1
        elif item==1:
            count_1+=1
        else:
            count_2+=1
    i=0
    while count_0>0:
        arr[i]=0
        i+=1
        count_0-=1
    while count_1 > 0:
        arr[i] = 1
        i += 1
        count_1 -= 1
    while count_2 > 0:
        arr[i] = 2
        i += 1
        count_2 -= 1
    return arr


arr=[0 ,2 ,1 ,2 ,0,0,2,2,1,2,2,0,1,0,0]
n=len(arr)
print(sortArray(arr,n))