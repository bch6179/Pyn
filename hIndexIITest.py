6 3 3 3 2 1
0 1 2 3 4 5
6 2 
6 6 6 6 6 6
    4
while l < h:
    m = l+ (h-l)/2
    
    if a[m] >= n-m -1 :
        l = m + 1
        index = l
     else:
        h = m - 1

return n - index 









