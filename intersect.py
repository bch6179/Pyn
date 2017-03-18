import collections
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 == None or nums2 == None: return None
        m1, m2 = collections.defaultdict(int),collections.defaultdict(int)
        res = []
        
        for num in nums1:
            m1[num] += 1
        for num in nums2:
            m2[num] += 1
        for k,v in m1.iteritems():
            if k in m2:
                n = min(v, m2[k])
                res.extend([k]*n) #([k for i in range(n)])
        return res
s = Solution() 
print s.intersect([11,11],[11,11])