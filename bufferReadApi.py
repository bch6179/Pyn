写一个API， allocate/release memory，每次allocate固定size， 要求可以重复 ... 给一个大buffer， 设计读写操作，判断越界，多线程，有点像read/write 

http://massivealgorithms.blogspot.com/2016/12/google-interview-misc-part-10.html

http://www.1point3acres.com/bbs/thread-210772-1-1.html
GG第一题就是给个数组，让你输出各种排列组合，简单DFS暴力搜索解决。
第二题给你一个从文件读数据的API(offset, bytestoread)，实现一个新的带buffer的API，这个API会多次调用，每次读的数据可以是文件中任意长度连续的一段，内存充足够用

这题扯了差不多十分钟才弄懂面试官的意思。至于用什么数据结构作buffer，写代码时从数组到列表再到双向队列改了好几遍，居然一直懵逼没想到用hashmap，小哥都不耐烦了，幸好在最后一刻还是说出了要用hashmap，然后时间到。明明这么水的题，才勉强做两个，而且第二题代码最后没写完，挂定了。。。
补充下第二题吧，就是给个API，从给定offset开始读bytestoread长度的数据。实现buffer型API让对同一文件多次读取效率提高（每次读也是从给定offset开始读给定长度的数据）

第二题的思路： 假设每次读的数据长度是n，然后hashmap的<key, value> = <index, buf> index = 0, n, 2*n, ...
然后以后每次从 x 处读len的数据，只需要取 hashmap.get(x / n) 中 x % n 开始的数据，如果 x % n != 0 则需要再加上 hashmap.get(x / n + 1) 中 0 ～ x % n的数据

大概就是这个意思，但每次读的长度和位置都不定，就用map<index,char>以字符为单位buffer就行了，题不难就是面试的时候费了好半天劲才明白什么意思

http://www.1point3acres.com/bbs/thread-210789-1-1.html