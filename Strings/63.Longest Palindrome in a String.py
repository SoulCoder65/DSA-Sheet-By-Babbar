def longestPalin(S):
    str_len=0
    longest_str=""
    for i in range(len(S)):
        #Odd Length
        l,r=i,i
        while l >=0 and r<len(S) and S[l]==S[r]:
            if (r-l+1)>str_len:
                longest_str=S[l:r+1]
                str_len=(r-l+1)
            l-=1
            r+=1
        # Even Length
        l, r = i, i+1
        while l >=0 and r<len(S) and S[l] == S[r]:
            if (r - l + 1) > str_len:
                longest_str = S[l:r + 1]
                str_len = (r - l + 1)
            l -= 1
            r += 1
    return longest_str

S="aaaabbaa"
print(longestPalin(S))