class Solution(object):
    #  BUCKET       思想是分成t+1个桶，对于一个数，将其分到第num / (t + 1) 个桶中，我们只需要查找相同的和相邻的桶的元素就可以判断有无重复。

# 比如t = 4，那么0~4为桶0，5~9为桶1，10~14为桶2  然后你懂的- –

 
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
       
        if k < 1 or t < 0:
            return False
            
     
        
        # for i in range(len(nums)):  #@mistake
        #     for val in range(nums[i] - t, nums[i] + t + 1):
        #         if val in hash:
        #             if abs(i - hash[val]) <= k:
        #                 return True
        #     hash[nums[i]] = i
        # return False
        
        dict = collections.OrderedDict()
        
        for x in range(len(nums)):
            key = nums[x]/max(1,t)
            for m in (key-1, key,key+1):
                if m in dict and abs(dict[m] - nums[x]) <= t:
                    return True
            dict[key] = nums[x]
            if x >= k:
                dict.popitem(last=False)
        return False

#     The idea is like the bucket sort algorithm. Suppose we have consecutive buckets covering the range of nums with each bucket a width of (t+1). If there are two item with difference <= t, one of the two will happen:

# (1) the two in the same bucket
# (2) the two in neighbor buckets
# For detailed explanation see my blog here

# Python

def containsNearbyAlmostDuplicate(self, nums, k, t):
    if t < 0: return False
    n = len(nums)
    d = {}
    w = t + 1
    for i in xrange(n):
        m = nums[i] / w
        if m in d:
            return True
        if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
            return True
        if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
            return True
        d[m] = nums[i]
        if i >= k: del d[nums[i - k] / w]
    return False

    def search(self, l, t, k):
        po = 0
        while po < len(l):
            i = po + 1
            while i < len(l):
                if abs(l[i][0] - l[po][0]) <= t and abs(l[i][1] - l[po][1]) <= k:
                    return True
                else:
                    if abs(l[i][0] - l[po][0]) > t:
                        break
                    else:
                        i +=1
            po += 1
        return False    
         
    # def bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
	# 	map<int, int> m;
	# 	for (int i = 0; i < nums.size(); i++) {
	# 		auto it = m.lower_bound(nums[i] - t);
	# 		if (it != m.end() &&  (long long int)it->first - (long long int)nums[i] <= t)
	# 			return true;
	# 		m[nums[i]] = i;
	# 		if (i >= k) m.erase(nums[i - k]);
	# 	}
	# 	return false;
	# }     
    def containsNearbyAlmostDuplicateON2(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        pp = sorted(zip(nums, range(len(nums))), key= lambda x:x[0])
        return self.search(pp,t ,k )
         
s = Solution() 
list1= [1, 13, 23,15]
list2=[2,2]
xs = "True" if s.containsNearbyAlmostDuplicate(list2, 3, 0) else "False"
print xs
    # def containsNearbyDuplicate(self, nums,t, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: bool
    #     """
    #     hash = {}
        
    #     for i in range(len(nums)):
    #         for val in range(nums[i] - t, nums[i] + t + 1):
    #             if val in hash:
    #                 if abs(i - hash[val]) <= k:
    #                     return True
    #         hash[nums[i]] = i
    #     return False

s = Solution() 
print s.containsNearbyDuplicate([-1,-1], 1, 0)
print s.containsNearbyDuplicate([1,6,22,2,7, 13], 1,2 )