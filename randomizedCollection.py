# I was initially just keeping a dictionary and a list and using list.remove() method.

# Just wanted to clarify the logic for other readers:

# The main idea of an efficient speedup is when removing an element. Here you find the index of the element to be deleted as the last item in its dictionary entry (which is a list).
# You then swap it with the actual last element in the numbers list you are maintaining. (Some corner cases need to be handled here).
# e.g. 1,2,3,1,5
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