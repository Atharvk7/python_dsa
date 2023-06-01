
a =[(7,8), (5,6), (1,3), (6,7)]
def mergeintervals(intervals,n):
    intervals.sort()     # here we are sorting the input array 
    if n == 0 or n == 1:
        return intervals
    i = 0
    end = n -1
    
    while(i<end):
            # If the intervals are mergeable here we merge them using extra array
            if(intervals[i][1]>=intervals[i+1][0] and intervals[i][1]<=intervals[i+1][1]):
                
                arr=[intervals[i][0],intervals[i+1][1]] # we are creating another array to store the values 
                intervals.remove(intervals[i])
                intervals.remove(intervals[i])
                
                intervals.insert(i,arr)
                end -= 1
                i -= 1
            # we checking if first interval is bigger or equal to second one then we can remove it 
            elif(intervals[i][1]>=intervals[i+1][0] and intervals[i][1]>=intervals[i+1][1]):
                
                intervals.remove(intervals[i+1])
                end-=1
                i-=1      
            i+=1
    return intervals
print(mergeintervals(a,len(a)))





