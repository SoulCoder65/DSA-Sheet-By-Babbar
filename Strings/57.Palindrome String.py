def checkPalindrone(S):
    S=list(S)
    l=0
    r=len(S)-1
    while l<r:
        if S[l]!=S[r]:
            return 0
        l+=1
        r-=1
    return 1



S="abba"
print(checkPalindrone(S))