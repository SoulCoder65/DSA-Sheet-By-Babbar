def rotationSubString(s1,s2):
    if len(s1)!=len(s2):
        return 0
    temp=s1+s1
    if s2 in temp:
        return 1
    return 0


s1="AACD"
s2="ACDA"
print(rotationSubString(s1,s2))
s1="ABCD"
s2="ACDB"
print(rotationSubString(s1,s2))
