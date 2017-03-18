class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        if not data: return True
        n = len(data); ind = 0
        while ind < n:
            m = self.countOne(data[ind])
            if ind + m > n: 
                return False
            elif m == 0:
                ind += 1
            elif m == 1 or m > 4: 
                return False
            else:
                for i in range(ind+1, ind+m):
                    if self.countOne(data[i]) != 1:
                        return False
            ind += m
        return True
        
    def countOne(self, num):
        count = 0
        for i in range(7, 0, -1):
            if num >> i & 1 == 1: count += 1
            else: break
        return count

public bool ValidUtf8(int[] data) {
    int bitCount = 0;
    
    foreach(int n in data){
        
        if(n >= 192){
            if(bitCount != 0)
                return false;
            else if(n >= 240)
                bitCount = 3;
            else if(n >= 224)
                bitCount = 2;
            else
                bitCount = 1;
        }else if(n >= 128){
            bitCount--;
            if(bitCount < 0)
                return false;
        }else if(bitCount > 0){
            return false;
        }
    }
    
    return bitCount == 0;
}

def check(nums, start, size):
    for i in range(start + 1, start + size + 1):
        if i >= len(nums) or (nums[i] >> 6) != 0b10: return False
    return True

class Solution(object):
    def validUtf8(self, nums, start=0):
        while start < len(nums):
            first = nums[start]
            if   (first >> 3) == 0b11110 and check(nums, start, 3): start += 4
            elif (first >> 4) == 0b1110  and check(nums, start, 2): start += 3
            elif (first >> 5) == 0b110   and check(nums, start, 1): start += 2
            elif (first >> 7) == 0:                                 start += 1
            else:                                                   return False
        return True
    def validUtf8(self, data):
        try:
        ''.join(map(chr, data)).decode('utf8')
        return True
    except Exception as e:
        return False