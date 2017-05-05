https://leetcode.com/problems/insert-delete-getrandom-o1/#/description

[LeetCode] Insert Delete GetRandom O(1) 常数时间内插入删除和获得随机数
 

Design a data structure that supports all following operations in average O(1) time.

 

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.


// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();


# I was initially just keeping a dictionary and a list and using list.remove() method.

# Just wanted to clarify the logic for other readers:

# The main idea of an efficient speedup is when removing an element. Here you find the index of the element to be deleted as the last item in its dictionary entry (which is a list).
# You then swap it with the actual last element in the numbers list you are maintaining. (Some corner cases need to be handled here).
# e.g. 1,2,3,  5  
# If you want to delete 1, swap it with 5 at the end of the list and shrink the list!

import random
import collections

class RandomizedCollection(object):

    def __init__(self):
        self.vals, self.idxs = [], collections.defaultdict(set)
        

    def insert(self, val):
        self.vals.append(val)
        self.idxs[val].add(len(self.vals) - 1)
        return len(self.idxs[val]) == 1
        

    def remove(self, val):
        if self.idxs[val]:
            out, ins = self.idxs[val].pop(), self.vals[-1]
            self.vals[out] = ins
            if self.idxs[ins]:
                self.idxs[ins].add(out)
                self.idxs[ins].discard(len(self.vals) - 1)
            

            self.vals.pop()
            return True
        return False 

    def getRandom(self):
        return random.choice(self.vals)
rc = RandomizedCollection()
rc.insert(1)
rc.insert(0)
rc.insert(1)
rc.insert(1)
rc.insert(1)
rc.insert(1)
rc.insert(1)
rc.insert(1)
rc.insert(0)
rc.remove(0)
rc.remove(0)
# he follow-up: allowing duplications.
# For example, after insert(1), insert(1), insert(2), getRandom() should have 2/3 chance return 1 and 1/3 chance return 2.
# Then, remove(1), 1 and 2 should have an equal chance of being selected by getRandom().

# The idea is to add a set to the hashMap to remember all the locations of a duplicated number.

# public class RandomizedSet {
# 	    ArrayList<Integer> nums;
# 	    HashMap<Integer, Set<Integer>> locs;
# 	    java.util.Random rand = new java.util.Random();
# 	    /** Initialize your data structure here. */
# 	    public RandomizedSet() {
# 	        nums = new ArrayList<Integer>();
# 	        locs = new HashMap<Integer, Set<Integer>>();
# 	    }
	    
# 	    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
# 	    public boolean insert(int val) {
# 	        boolean contain = locs.containsKey(val);
# 	        if ( ! contain ) locs.put( val, new HashSet<Integer>() ); 
# 	        locs.get(val).add(nums.size());        
# 	        nums.add(val);
# 	        return ! contain ;
# 	    }
	    
# 	    /** Removes a value from the set. Returns true if the set contained the specified element. */
# 	    public boolean remove(int val) {
# 	        boolean contain = locs.containsKey(val);
# 	        if ( ! contain ) return false;
# 	        int loc = locs.get(val).iterator().next();
#                 locs.get(val).remove(loc);
# 	        if (loc < nums.size() - 1 ) {
# 	            int lastone = nums.get(nums.size() - 1 );
# 	            nums.set( loc , lastone );
# 	            locs.get(lastone).remove(nums.size() - 1);
# 	            locs.get(lastone).add(loc);
# 	        }
# 	        nums.remove(nums.size() - 1);
# 	        if (locs.get(val).isEmpty()) locs.remove(val);
# 	        return true;
# 	    }
	    
# 	    /** Get a random element from the set. */
# 	    public int getRandom() {
# 	        return nums.get( rand.nextInt(nums.size()) );
# 	    }
# 	}

复制代码
class RandomizedSet {
public:
    /** Initialize your data structure here. */
    RandomizedSet() {}
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if (m.count(val)) return false;
        nums.push_back(val);
        m[val] = nums.size() - 1;
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if (!m.count(val)) return false;
        int last = nums.back();
        m[last] = m[val];
        nums[m[val]] = last;
        nums.pop_back();
        m.erase(val);
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        return nums[rand() % nums.size()];
    }
private:
    vector<int> nums;
    unordered_map<int, int> m;
};

    这道题让我们在常数时间范围内实现插入删除和获得随机数操作，如果这道题没有常数时间的限制，那么将会是一道非常简单的题，我们直接用一个set就可以搞定所有的操作。但是由于时间的限制，我们无法在常数时间内实现获取随机数，所以只能另辟蹊径。此题的正确解法是利用到了一个一维数组和一个哈希表，其中数组用来保存数字，哈希表用来建立每个数字和其在数组中的位置之间的映射，对于插入操作，我们先看这个数字是否已经在哈希表中存在，如果存在的话直接返回false，不存在的话，我们将其插入到数组的末尾，然后建立数字和其位置的映射。删除操作是比较tricky的，我们还是要先判断其是否在哈希表里，如果没有，直接返回false。由于哈希表的删除是常数时间的，而数组并不是，为了使数组删除也能常数级，我们实际上将要删除的数字和数组的最后一个数字调换个位置，然后修改对应的哈希表中的值，这样我们只需要删除数组的最后一个元素即可，保证了常数时间内的删除。而返回随机数对于数组来说就很简单了，我们只要随机生成一个位置，返回该位置上的数字即可，参见代码如下：

 