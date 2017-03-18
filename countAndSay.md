1. set res = '' for next iteration #Mistake Need to init here, so that the temp not get from previous ones
2. don't forget add last one after loop terminate        res+=str(count)+prev #last one
3.  set dummy value in previous when looking backward ;  looking forward need to minus-1
 prev = '#'
        res = ''  
        for cur in prev:
            if cur == prev:
            else:
                if cur != '#': 

 i = 0
        res = ''   
        while i < m-1:  
            if prev[i] == prev[i+1]: