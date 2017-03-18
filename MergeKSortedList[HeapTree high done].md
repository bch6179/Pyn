[Note]
======
 0) heap
 1) while k > 0:
        start = 0
        end = k
        while start < end:
            merge2
            start++, end--
            adjust k =   end if start <= end
    8/4 4/2 /2/1     4*n+ 2*2n+1*4n    8nlog8, knlogk
2) d&d 
 
======
 Time complexity of this solution would be O(nk Log k
Divide and Conquer approach is discussed. This approach doesn’t require extra space for heap and works in O(nk Log k)
Time Complexity of above algorithm is O(nk logk) as outer while loop in function mergeKLists() runs log k times and every time we are processing nk elements.
 
 This *text* has a [link to wikipedia](http://wikipedia.org/)
 
 Merge k sorted linked lists and return it as one sorted list. [Java]
1) First think about a simple merge idea. Go through k head elements each time, they are the smallest among their list, k pointers and totally nk elements.
time: O(nk^2) space:O(k);
[CODE] 略，自己写一下把，这个简单
 
2) Use heap. This is a classic question for heap. each time we change a heap value we only use Log(k) time 
time: O(nkLogk) space:O(k)
 
1) A comparator used can be pass
ed to Collections.sort(coll,comparator) 
2) In java, heap is implemented as PriorityQueue. The constructor
PriorityQueue(int initialCapacity, Comparator<? super E> comparator)
constructor is initialized with capacity and compare rule.
3) Java anonymous class is used to simply create and use this comparator 
4) The node inside list could be null
5) PriorityQueue use poll() method to pop out it’s first element
K
1、这一题明显是考Heap的，如果对Java PriorityQueue不够了解的，就应该去复习一下。Java7和Java8不太一样，Java8在传入comparator不再需要给定size。
2、代码中写到了Collections.sort()，和在sort中写匿名类。
3、为什么要写dummy？在那些题中需要写dummy而return dummy.next。那些题不需要？
4、为什么用Queue interface，用List－>LinkedList可以吗，是否要复习总结一下list，queue和它们的implementation? 如果对Object Oriented 不熟悉的，是否要再看看继承(Inheritence)和多态(Polymorphism)。那再往深处想一想，Abstract Class 和 Interface 的区别，优缺点呢？
>
这些 Java 基础就是做题的时候要想，不是很理解就要及时解决。基础不好的同学，刚开始做会比较慢，所以一道题做完过去了大半天，这很正常，等做多了，烂熟于心了，做题就快了。每次做题也都是对知识点的强化。

代码[CODE]部分和代码上面我自己的思考笔记都是写在Evernote上的，每次写完代码要把遇到这个题时候的想法，解题思路，看完别人答案之后自己的理解，基于答案对自己code的改进写进去。

[Code]
======

 ```java
import java.util.*;

/**
 * Merge k sorted linked lists and return it as one sorted list. Analyze and
 * describe its complexity.
 * 
 * Tags: Divide and Conquer, Linkedlist, Heap
 */
class MergeKSortedList {
    public static void main(String[] args) {
        
    }
    
    /**
     * Use a heap, O(n * log(k))
     */
    public ListNode mergeKLists(List<ListNode> lists) {
        if (lists == null || lists.size() == 0) return null;
        // Build priority queue
        Queue<ListNode> queue = new PriorityQueue<ListNode>(lists.size(), new Comparator<ListNode>() {
            @Override
            public int compare(ListNode n1, ListNode n2) {
                return n1.val - n2.val;
            }
        });
        for (ListNode n : lists) if (n != null) queue.add(n);
        
        ListNode dummy = new ListNode(0); // set dummy head
        ListNode tail = dummy;
        while (!queue.isEmpty()) { // build next
            tail.next = queue.poll();
            tail = tail.next;
            if (tail.next != null) queue.add(tail.next);
        }
        return dummy.next;
    }
    
    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }
    
    /**
     * Divide and conquer
     * merge two halves, divide to merge two lists
     */
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        
        // next node should be the result of comparison
        if (l1.val < l2.val) {
            l1.next = mergeTwoLists(l1.next, l2); // notice l1.next
            return l1;
        } else {
            l2.next = mergeTwoLists(l1, l2.next); // notice l2.next
            return l2;
        }
    }

    public ListNode mergeKLists(List<ListNode> lists) {
        /*base cases*/
        if (lists.size() == 0) return null;
        if (lists.size() == 1) return lists.get(0);
        if (lists.size() == 2) return mergeTwoLists(lists.get(0), lists.get(1));
        /*merge two halves*/
        return mergeTwoLists(mergeKLists(lists.subList(0, lists.size()/2)), 
            mergeKLists(lists.subList(lists.size()/2, lists.size())));
    }
   
}

public class Solution {
    /**
     * @param lists: a list of ListNode
     * @return: The head of one sorted list.
     */
    public ListNode mergeKLists(List<ListNode> lists) {
        if (lists.size() == 0) {
            return null;
        }
        return mergeHelper(lists, 0, lists.size() - 1);
    }
    
    private ListNode mergeHelper(List<ListNode> lists, int start, int end) {
        if (start == end) {
            return lists.get(start);
        }
        
        int mid = start + (end - start) / 2;
        ListNode left = mergeHelper(lists, start, mid);
        ListNode right = mergeHelper(lists, mid + 1, end);
        return mergeTwoLists(left, right);
    }
    
    private ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                tail.next = list1;
                tail = list1;
                list1 = list1.next;
            } else {
                tail.next = list2;
                tail = list2;
                list2 = list2.next;
            }
        }
        if (list1 != null) {
            tail.next = list1;
        } else {
            tail.next = list2;
        }
        
        return dummy.next;
    }
}
// Version 3: merge two by two
/**
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
 */ 
public class Solution {
    /**
     * @param lists: a list of ListNode
     * @return: The head of one sorted list.
     */
    public ListNode mergeKLists(List<ListNode> lists) {  
        if (lists == null || lists.size() == 0) {
            return null;
        }
        
        while (lists.size() > 1) {
            List<ListNode> new_lists = new ArrayList<ListNode>();
            for (int i = 0; i + 1 < lists.size(); i += 2) {
                ListNode merged_list = merge(lists.get(i), lists.get(i+1));
                new_lists.add(merged_list);
            }
            if (lists.size() % 2 == 1) {
                new_lists.add(lists.get(lists.size() - 1));
            }
            lists = new_lists;
        }
        
        return lists.get(0);
    }
    
    private ListNode merge(ListNode a, ListNode b) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (a != null && b != null) {
            if (a.val < b.val) {
                tail.next = a;
                a = a.next;
            } else {
                tail.next = b;
                b = b.next;
            }
            tail = tail.next;
        }
        
        if (a != null) {
            tail.next = a;
        } else {
            tail.next = b;
        }
        
        return dummy.next;
    }
}

```