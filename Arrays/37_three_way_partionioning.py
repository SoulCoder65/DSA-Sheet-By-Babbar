def ThreeWayPartition(array,a,b):
    l=0
    r=len(array)-1

    for i in range(len(array)):
        if array[i]<a:
            array[l],array[i]=array[i],array[l]
            l+=1
        elif array[i]>b:
            array[i],array[r]=array[r],array[i]
            r-=1
            i-=1
    return array


array=[1, 2, 3, 3, 4]
a=1
b=2
print(ThreeWayPartition(array,a,b))