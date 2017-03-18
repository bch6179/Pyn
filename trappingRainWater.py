# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

#Calculate the rightmost max table : prepare and conquer for the method of finding the rightmost taller one and go back to pop stack
#Shrinking the right window as quick sort method, to save time

# For index i, the water volume of i: vol_i = min(left_max_i, right_max_i) - bar_i.

# The left_max array from left to right is always non-descending, the right_max is non-ascending.

# Having such observation, we can say:

# Given i < j, if left_max_i <= right_max_j: vol_i = left_max_i - bar_i, otherwise, vol_j = right_max_j - bar_j
# because, if left_max_i <= right_max_j: left_max_i <= right_max_j <= right_max_j-1 <= ... <= right_max_i, then min(left_max_i, right_max_i) is always left_max_i

# Code is pasted.

def trap1(self, bars):
    if not bars or len(bars) < 3:
        return 0
    volume = 0
    left, right = 0, len(bars) - 1
    l_max, r_max = bars[left], bars[right]
    while left < right:
        l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
        if l_max <= r_max:
            volume += l_max - bars[left]
            left += 1
        else:
            volume += r_max - bars[right]
            right -= 1
    return volume

def trap2(bars):
    if (len(bars) <= 1): return 0

    rightMax = [0] * len(bars)
    maxSoFar = 0
    res = 0
    for i in reversed(range(len(bars))):
        maxSoFar = max(bars[i], maxSoFar)
        rightMax[i] = maxSoFar
    maxSoFar = bars[0]
    for i in range(0, len(bars)):
        maxSoFar = max(bars[i], maxSoFar)
        t = min(maxSoFar, rightMax[i]) - bars[i]
        res += t if t > 0 else 0
    return res
def trap4(bars):
        """
        :type height: List[int]
        :rtype: int
        """
        if (len(bars) <= 1): return 0
        left, right = 0, len(bars)-1
        maxLeftSoFar,maxRightSoFar = bars[left], bars[right]
        res = 0
 
        while left < right:
            maxLeftSoFar = max(bars[left], maxLeftSoFar)
            maxRightSoFar = max(maxRightSoFar, bars[right])
            # if maxLeftSoFar > bars[left]:
            if maxLeftSoFar <= maxRightSoFar:
                res += maxLeftSoFar - bars[left]
                left += 1
            # elif maxRightSoFar > bars[right]:
            else:
                res += maxRightSoFar - bars[right]
                right -= 1
            # else:
            #     left += 1
            #     right -=1
        return res
def trap(bars):
    n = len(bars)
    if n < 3: return 0
    s = [0]
    res = 0
    
    for i in range(1,n):
        if bars[i] > bars[s[-1]]: #see a 4 > 1, increasement
            bottom = bars[s[-1]]
            s.pop()
            while  s and bars[i] >= bars[s[-1]]: # pop the previous equal or smaller one and accumulate, stop at preivous 5
                res += (bars[s[-1]] - bottom)*(i-s[-1]-1)
                bottom = bars[s[-1]]
                s.pop()    # get (5-4) * (6-2-1) = 3
            if s: # s still has sth bigger than the last bottom 5 (last popped above), need to get the 4 part, but here is 0; if empty, then no need to add 
                res += (bars[i]- bottom) * (i -s[-1]-1)
        s.append(i)  # 5 4  
    return res

print trap([1,5,3,1,4,7])