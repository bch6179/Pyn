#Mistake
1.  j wrongly write to i in another loop
2. skip answers, when removing duplicates, only remove those added, so compare backward. consider the -2 -2 itself part of the answer
# j  k this will skip
                while ( j < k and i != j-1 and nums[j] == nums[j-1]): j+=1 # 1 1  , so not j+1, but j-1
               #                                      i   j      k this will skip one solution  
                #[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]  -2 -2 . 3 6