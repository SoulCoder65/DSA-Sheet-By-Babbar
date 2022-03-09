def find_median(v):
    v.sort()
    length=len(v)
    if length%2 != 0:
        return v[length//2]
    else:

        return (v[length//2-1]+v[length//2])//2


v=[56 ,67 ,30 ,79]
print(find_median(v))