There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
https://leetcode.com/problems/gas-station/?tab=Description

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0 or len(cost) == 0 or sum(gas) < sum(cost):
            return -1
        position = 0
        balance = 0 # current tank balance
        total = 0
        for i in range(len(gas)):
            balance += gas[i] - cost[i] # update balance
            if balance < 0: # balance drops to negative, reset the start position
               total += balance

                balance = 0 #Mistake
                position = i+1
        return position if total +balance >= 0 else -1
    def canCompleteCircuit(self, gas, cost):
        gas_left = gas_needed = start = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            gas_left += g - c
            if gas_left < 0:
                gas_needed -= gas_left
                start = i + 1
                gas_left = 0
        return start if gas_left >= gas_needed else -1
If car starts at A and can not reach B. Any station between A and B
can not reach B.(B is the first station that A can not reach.)
If the total number of gas is bigger than the total number of cost. There must be a solution.
(Should I prove them?)

Every time a fail happens, accumulate the amount of gas that is needed to overcome the fail. After looping through the stations, if the gas left is more than gas needed, then we have a solution, otherwise not.
