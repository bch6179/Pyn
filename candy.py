https://leetcode.com/problems/candy/?tab=Description

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Subscribe to see which companies asked this question.

Hide Tags
e first one is O(n) space, but very concise. The idea is to find the mininum candies for each child considering only left or right neighbors.

class Solution:
# @param ratings, a list of integer
# @return an integer
def candy(self, ratings):
    candies = [1] * len(ratings)
    for i in xrange(len(ratings) - 1):
        if ratings[i + 1] > ratings[i]:
            candies[i + 1] = max(candies[i + 1], candies[i] + 1)
            
        j = -i - 1
        if ratings[j - 1] > ratings[j]: 
            candies[j - 1] = max(candies[j - 1], candies[j] + 1)
    
    return sum(candies)
public int candy(int[] ratings) {
    int candies[] = new int[ratings.length];        
    Arrays.fill(candies, 1);// Give each child 1 candy 
    	
    for (int i = 1; i < candies.length; i++){// Scan from left to right, to make sure right higher rated child gets 1 more candy than left lower rated child
        if (ratings[i] > ratings[i - 1]) candies[i] = (candies[i - 1] + 1);
    }
     # 2 3 1 6 
     # 1 2 1 2
    for (int i = candies.length - 2; i >= 0; i--) {// Scan from right to left, to make sure left higher rated child gets 1 more candy than right lower rated child
	    if (ratings[i] > ratings[i + 1]) candies[i] = Math.max(candies[i], (candies[i + 1] + 1));
    }
    
    int sum = 0;        
    for (int candy : candies)  
    	sum += candy;        
    return sum;
}