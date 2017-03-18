map[s[-1]] #Mistake map is not callable
1. prev / cur
 prev = 0
        for n in reversed(s):
            cur = map[n]
            sum += -1*cur if cur < prev else cur
            prev = cur
        return sum

2. Index
index = len(s)-2
        cur = 0
        while index >= 0:
            if map[s[index]] >= map[s[index+1]]:


Symbol	I	V	X	L	C	D	M
Value	1	5	10	50	100	500	1,000


I, II, III, IV, V, VI, VII, VIII, IX, X.
Numbers are formed by combining symbols and adding the values, so II is two (two ones) and XIII is thirteen (a ten and three ones). Because each numeral has a fixed value rather than representing multiples of ten, one hundred and so on, according to position, there is no need for "place keeping" zeros, as in numbers like 207 or 1066; those numbers are written as CCVII (two hundreds, a five and two ones) and MLXVI (a thousand, a fifty, a ten, a five and a one).

Symbols are placed from left to right in order of value, starting with the largest. However, in a few specific cases,[2] to avoid four characters being repeated in succession (such as IIII or XXXX), subtractive notation is used: as in this table:[3][4]

Number	4	9	40	90	400	900
Notation	IV	IX	XL	XC	CD	CM
