Thinking boldly and broadly by adding one more state of buying
if you buy, neg profit , then when you 
sell, prev_buy+prices[i] or s[i-1]
b  s[i-1]-prices[i] or b[i-1]
instead of F[n-3] + pc-p1 and confused at the initialization, since F[n-3] has two+states or dependencies

just like product sum, has one more possible from the min negative

# Of course one may come up with a O(1) space solution directly, but I think it is better to be generous when you think and be greedy when you implement.

# The natural states for this problem is the 3 possible transactions : buy, sell, rest. Here rest means no transaction on that day (aka cooldown).