class Solution(object):
    def merge(self, nums1, m, nums2, n):
        toInsert = m + n - 1
        i, j = m-1, n-1

        while toInsert >= 0 and i >= 0 and j >= 0:
            if nums1[i] > nums2[j]: 
                nums1[toInsert] = nums1[i]
                i -= 1
            else:
                nums1[toInsert] = nums2[j]
                j -= 1
            toInsert -= 1

        while j >= 0 and toInsert >= 0:
            nums1[toInsert] = nums2[j]
            j -= 1  
            toInsert -= 1

        return nums1
    def merge2(self, nums1, m, nums2, n):
        i, j = m-1, n-1
        while  i >= 0 and j >= 0:
            if nums1[i] > nums2[j]: 
                nums1[i+j+1] = nums1[i]
                i -= 1
            else:
                nums1[i+j+1] = nums2[j]
                j -= 1

        while j >= 0:
            nums1[i+j+1]= nums2[j]
            j -= 1  
s = Solution()
print(s.merge([1],1, [],0))
#print(s.merge([1,3,7, 9, 10,11,12],4, [2,4,6],3))