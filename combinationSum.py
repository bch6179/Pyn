class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs_I(candidates, list, target, pos):
            if target < 0:
                return
            if target == 0:
                res.append(list[:]) #Mistake list not hashable, result has duplicates answer 2 2 3, 2 3 2
                return
            i = pos
            while i < len(candidates) and target >= candidates[i]:
                num = candidates[i]
                #list.append(num)
                dfs(candidates, list+[num], target - num,i)
                #list.pop()  #Mistake FORGOT POP
                i += 1

#    unique combinations in C where the candidate numbers sums to T. Each number in C may only be used once in the combination.
        def dfs_II(candidates, list, target, pos):
  
            if target == 0:
                res.append(list[:])  
                return
            i = pos
            while i < len(candidates) and target >= candidates[i]:
                num = candidates[i]
                #list.append(num)
                if i == pos or num != candidates[i-1]: #to avoid duplicate  1 7 since the first one might already have
                    dfs(candidates, list+[num], target - num,i+1)
                #list.pop()
                i += 1

                # Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


    def combinationSum3(self, k, n):
        def dfs1(self, nums, k, n, index, path, res):
            if k < 0 or n < 0: # backtracking 
                return 
            if k == 0 and n == 0: 
                res.append(path)
            for i in xrange(index, len(nums)):
                self.dfs(nums, k-1, n-nums[i], i+1, path+[nums[i]], res)
        def dfs(candidates, k, target, list, pos):
           #Mistake pos should not k for end
            if target == 0 and k == 0:
                res.append(list[:]) 
                return
            i = pos
            while i < len(candidates) and target >= candidates[i]:
                num = candidates[i]
                #list.append(num)
                if i == pos or num != candidates[i-1]:
                    dfs(candidates, k-1, target - num, list+[num], i+1)
                #list.pop()
                i += 1
        res = []   
        dfs(xrange(1,10),k, n, [], 0 ) #Mistake it doesn't mean xrange from 1 to n
        return  res 
    def combinationSum4_dfs(self, nums, target):
        def dfs_notwork(candidates, list, target, visited): #not considering 1 1 1 1, reusable 1
            if target == 0:
                res.append(list[:])  
                return
            i = 0
            while i < len(candidates):
                if not visited[i]:
                    num = candidates[i]
                    #list.append(num)
                    visited[i] = True
                    dfs(candidates, list+[num], target - num, visited)
                    visited[i] = False

                    #list.pop()
                i += 1
        def dfs(candidates, target, mem):
            if target <= 0:
                return 1 if target == 0 else 0 #Mistake target < 0 , also need to return
            if mem[target] != -1: return mem[target]
            rt = 0

            for num in nums:
                rt += dfs(candidates, target - num,mem)
            mem[target] = rt 
            return rt 
            #Mistake not return mem[target]
           
       
        mem = [-1 for i in range(target+1)]
        return dfs(nums, target, mem)
    def combinationSum4(self, nums, target):
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(1, target + 1):
            for num in nums:
                if num  > i: break
                if num == i: combs[i] += 1
                if num  < i: combs[i] += combs[i - num]
        return combs[target]
 #Mistake[1,2,3] 4 ,it will not work if reversed i and num loop
 #you could save <= i
s = Solution()
print s.combinationSum4([1,2, 4, 7], 7)   

print s.combinationSum4([3,2, 4, 7], 7)   
#print s.combinationSum3(3, 9)  