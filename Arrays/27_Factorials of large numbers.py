def largestFact(num):
    if num<=1:
        return num
    return num*largestFact(num-1)

num=3
print(largestFact(num))