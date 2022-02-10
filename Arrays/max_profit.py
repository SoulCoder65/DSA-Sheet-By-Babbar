def max_profit(arr):
    i,j=0,1
    maxProfit=0
    while j<len(arr):
        if arr[i]<arr[j]:
            profit=arr[j]-arr[i]
            maxProfit=max(profit,maxProfit)

        else:
            i=j
        j+=1
    return maxProfit

arr=[7,6,4,3,1]

print(max_profit(arr))