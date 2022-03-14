def countAndSay(n):
    if n==1:return "1"
    if n==2:return "11"
    s="11"
    for i in range(3,n+1):
        t=""
        count=1
        s=s+"$"
        for j in range(1,len(s)):
            if s[j]!=s[j-1]:
                t+=str(count)
                t+=s[j-1]
                count=1
            else:
                count+=1
        s=t
    return s

n=4
print(countAndSay(4))