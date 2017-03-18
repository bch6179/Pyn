https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/?tab=Description

Read N Characters Given Read4 II - Call multiple times Add to List
Description  Submission  Solutions
Total Accepted: 21971 Total Submissions: 90003 Difficulty: Hard Contributors: Admin
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

public class Solution extends Reader4 {
    public int read(char[] buf, int n) {
        int i = 0;
        while (i < n && (i4 < n4 || (i4 = 0) < (n4 = read4(buf4))))
            buf[i++] = buf4[i4++];
        return i;
    }
    char[] buf4 = new char[4];
    int i4 = 0, n4 = 0;
}
(i4 = 0) < (n4 = read4(buf4)) is super smart. It is shortcut of when buf4 is used up, we reload buf4: (n4 = read4(buf4)) > 0 and i4 = 0.

public int read(char[] buf, int n) {      // this question is about internal buffer and external buffer
    // internal buffer: i4, n4, buf4
    // external buffer: i, n, buf
        int i = 0;
        while (i < n) {     // external buf limitation
            if (i4 >= n4) {     // internal buf limitation
                i4 = 0;
                n4 = read4(buf4);
                if (n4 == 0) break;
            }
            buf[i++] = buf4[i4++];
        }
        return i;
    }
    char[] buf4 = new char[4];
    int i4 = 0, n4 = 0;
    
public int read(char[] buf, int n) {      // this question is about internal buffer and external buffer
    // internal buffer: i4, n4, buf4
    // external buffer: i, n, buf
        int i = 0;
        while (i < n) {     // external buf limitation
            if (i4 >= n4) {     // internal buf limitation
                i4 = 0;
                n4 = read4(buf4);
                if (n4 == 0) break;
            }
            buf[i++] = buf4[i4++];
        }
        return i;
    }
    char[] buf4 = new char[4];
    int i4 = 0, n4 = 0;


二题给你一个从文件读数据的API(offset, bytestoread)，实现一个新的带buffer的API，这个API会多次调用，每次读的数据可以是文件中任意长度连续的一段，内存充足够用

就是给个API，从给定offset开始读bytestoread长度的数据。实现buffer型API让对同一文件多次读取效率提高（每次读也是从给定offset开始读给定长度的数据）


tructure is from this post

IMHO, the above solution cannot handle a few problems:

if there are lots of read(1) or read(2), the queue becomes increasingly large

the queue is extend by size of 4 in each call, and "" can be wrote into queue even it doesn't exist in file

Here is my modified algorithm with commons..

def __init__(self):
    self.queue = [] # global "buffer"

def read(self, buf, n):
    idx = 0

    # if queue is large enough, read from queue
    while self.queue and n > 0:
        buf[idx] = self.queue.pop(0)
        idx += 1
        n -= 1
    
    while n > 0:
        # read file to buf4
        buf4 = [""]*4
        l = read4(buf4)

        # if no more char in file, return
        if not l:
            return idx

        # if buf can not contain buf4, save to queue
        if l > n:
            self.queue += buf4[n:l]

        # write buf4 into buf directly
        for i in range(min(l, n)):
            buf[idx] = buf4[i]
            idx += 1
            n -= 1
    return idx