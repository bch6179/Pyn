class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        map = {100:'C', 99:'IC', 50:'L', 49:'IL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I' }
        res = []
        while num > 0:
            for key, val in map:
                v = num / key
                if v == 0: continue
                res += val*v
                num = num % key
        return res
     # @param {integer} num
    # @return {string}
    def parse(self, digit, index):
        NUMS = {
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX',
        }
        ROMAN = {
            'I': ['I', 'X', 'C', 'M'],
            'V': ['V', 'L', 'D', '?'],
            'X': ['X', 'C', 'M', '?']
        }
        
        s = NUMS[digit]
        return s.replace('X', ROMAN['X'][index]).replace('I', ROMAN['I'][index]).replace('V', ROMAN['V'][index])
        
    def intToRoman(self, num):
        s = ''
        index = 0
        while num != 0:
            digit = num % 10
            if digit != 0:
                s = self.parse(digit, index) + s
            num = num / 10
            index += 1
        return s
            