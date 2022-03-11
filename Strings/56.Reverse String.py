def reverseString(string):
    l=0
    r=len(string)-1
    while l<r:
        string[l],string[r]=string[r],string[l]
        l+=1
        r-=1
    return string

string=list("abcdefg")

print(reverseString(string))