class Solution(object):
    def reverse(self,digits):
        start, end = 0, len(digits)-1
        while start < end:
            temp = digits[end]
            digits[end] = digits[start]
            digits[start] = temp
            start+=1
            end-=1
        return digits
        
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #999
        #1090 
        
        carry = 1
        for i, d in reversed(list(enumerate(digits))):
            d += carry
            if d == 10:
                digits[i]= 0
                carry = 1
            else: digits[i] = d;carry = 0;break
        if carry == 1:
            digits[0] = 1
            digits.append(0)
        return digits
        
   def plusOne2(self, digits):
        digits = list(reversed(digits))
        digits[0] += 1
        i, carry = 0, 0
        while i < len(digits):
            next_carry = (digits[i] + carry) / 10
            digits[i] = (digits[i] + carry) % 10
            i, carry = i + 1, next_carry
        if carry > 0:
            digits.append(carry)
        
        return list(reversed(digits))