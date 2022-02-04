def mergeIntervals(intervals,n):
    intervals.sort()
    output=[intervals[0]]

    for start,end in intervals[1:]:
        lastend=output[-1][1]
        if start<=lastend:
            output[-1][1]=max(lastend,end)
        else:
            output.append([start,end])
    return output


arr=[[1,3],[2,6],[8,10],[15,18]]
print(mergeIntervals(arr,len(arr)))