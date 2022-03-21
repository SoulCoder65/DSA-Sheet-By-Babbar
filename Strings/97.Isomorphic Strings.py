def areIsomorphic(str1,str2):
    str1Map={}
    str2Map={}
    for i in range(len(str1)):
        c1,c2=str1[i],str2[i]
        if (((c1 in str1Map) and str1Map[c1]!=c2 ) or ((c2 in str1Map) and str2Map[c2]!=c1)):
            return False
        str1Map[c1]=c2
        str2Map[c2]=c1
    return True

# def areIsomorphic(pattern,s):
#     str1Map={}
#     str2Map={}
#     s=s.split(" ")
#     print(
#     for i in range(len(pattern)):
#         char1=pattern[i]
#         elem1=s[i]
#         if ( ((char1 in str1Map) and str1Map[char1]!=elem1) or ((elem1 in str2Map) and str2Map[elem1]!=char1) ):
#             return False
#         str1Map[char1]=elem1
#         str2Map[elem1]=char1
#     return True

str1="abba"
str2="dog cat cat dog"
print(areIsomorphic(str1,str2))