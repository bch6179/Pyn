# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read1(self, buf, n):
        i = 0
        while i < n: 
            buf4 = ['','','','']
            count = read4(buf4) # Read file into buf4.
            if not count: break # EOF
            count = min(count, n - i)
            #buf[i:] = buf4[:count] # Copy from buf4 to buf.
            buf[i:]  = buf4[:count]
            i += count
        return i
    def read2MyBad(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        count = 0
        while n > 0:
            sub = ['','','',''] #need this format to reserve spaces , otherwise index error
            k = read4(sub)
            buf += sub   #copy not work, #copy the min of need and actual
            count += k    
            if k < 4:
                break
        return count

        def __init__(self):
            self.queue = []
    def read2(self, buf, n):
        read, need, buffer = 0, n, ['']*4
        while need > 0:
            k = read4(buffer)
            self.queue.extend(buffer[:k])
            need = min(len(self.queue), n - read)
            buf[read:read+need] = [self.queue.pop(0) for _ in xrange(need)]
            read += need
        return read
  
    def read(self, buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Maximum number of characters to read (int)
    :rtype: The number of characters read (int)
    """
        need = n
        i = 0
        while need > 0:
            buf4 = ['']*4
            r = read4(buf4)
            if not r:
                break  #Mistake missing break
            actual = min(r, need)
            buf[i:actual]= buf4[:actual]
            #mistake buf.extend() will overwrite buf?
            i += actual
            need -= actual
            
        return i