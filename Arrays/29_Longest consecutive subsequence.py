def longestConsecutiveSubsequence(nums,N):
    longest=0
    set_nums=set(nums)
    for item in nums:
        if (item-1) not in set_nums:
            length=0
            while (item+length) in set_nums:
                length+=1
            longest=max(longest,length)
    return longest

nums=[2,6,1,9,4,5,3]
N=len(nums)
print(longestConsecutiveSubsequence(nums,N))
