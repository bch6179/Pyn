Rejection Sampling
November 7, 2010 by 1337c0d3r    29 Replies
Given a function which generates a random integer in the range 1 to 7, write a function which generates a random integer in the range 1 to 10 uniformly.

This appear to be one of those probabilistic analysis questions. You should be familiar with the concept of expected value, as it could be extremely helpful in probabilistic analysis.

Hint:
Assume you could generate a random integer in the range 1 to 49. How would you generate a random integer in the range of 1 to 10? What would you do if the generated number is in the desired range? What if it’s not?

Solution:
This solution is based upon Rejection Sampling. The main idea is when you generate a number in the desired range, output that number immediately. If the number is out of the desired range, reject it and re-sample again. As each number in the desired range has the same probability of being chosen, a uniform distribution is produced.

Obviously, we have to run rand7() function at least twice, as there are not enough numbers in the range of 1 to 10. By running rand7() twice, we can get integers from 1 to 49 uniformly. Why?

   1  2  3  4  5  6  7
1  1  2  3  4  5  6  7
2  8  9 10  1  2  3  4
3  5  6  7  8  9 10  1
4  2  3  4  5  6  7  8
5  9 10  1  2  3  4  5
6  6  7  8  9 10  *  *
7  *  *  *  *  *  *  *
A table is used to illustrate the concept of rejection sampling. Calling rand7() twice will get us row and column index that corresponds to a unique position in the table above. Imagine that you are choosing a number randomly from the table above. If you hit a number, you return that number immediately. If you hit a *, you repeat the process again until you hit a number.

Since 49 is not a multiple of tens, we have to use rejection sampling. Our desired range is integers from 1 to 40, which we can return the answer immediately. If not (the integer falls between 41 to 49), we reject it and repeat the whole process again.


1
2
3
4
5
6
7
8
9
int rand10() {
  int row, col, idx;
  do {
    row = rand7();
    col = rand7();
    idx = col + (row-1)*7;
  } while (idx > 40);
  return 1 + (idx-1)%10;
}
Now let’s get our hands dirty to calculate the expected value for the number of calls to rand7() function.

E(# calls to rand7) = 2 * (40/49) +
                      4 * (9/49) * (40/49) +
                      6 * (9/49)2 * (40/49) +
                      ...

                      ∞
                    = ∑ 2k * (9/49)k-1 * (40/49)
                      k=1

                    = (80/49) / (1 - 9/49)2
                    = 2.45
Optimization:
There are a total of 2.45 calls to rand7() on average using the above method. Can we do better? Glad that you asked. In fact, we are able to improved the above method by 10% faster.

It seems wasteful to throw away the integers in the range 41 to 49. In fact, we could reuse them in the hope of minimizing the number of calls to rand7(). In the event that we could not generate a number in the desired range (1 to 40), it is equally likely that each number of 41 to 49 would be chosen. In other words, we are able to obtain integers in the range of 1 to 9 uniformly. Now, run rand7() again and we obtain integers in the range of 1 to 63 uniformly. Apply rejection sampling where the desired range is 1 to 60. If the generated number is in the desired range (1 to 60), we return the number. If it is not (61 to 63), we at least obtain integers of 1 to 3 uniformly. Run rand7() again and we obtain integers in the range of 1 to 21 uniformly. The desired range is 1 to 20, and in the unlikely event we get a 21, we reject it and repeat the entire process again.

Below is the code for this optimized method. Note that there are code sections that are repeated, but I leave it as it is for code clarity. (Take it as a challenge to refactor the code below!)


1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
int rand10Imp() {
  int a, b, idx;
  while (true) {
    a = rand7();
    b = rand7();
    idx = b + (a-1)*7;
    if (idx <= 40)
      return 1 + (idx-1)%10;
    a = idx-40;
    b = rand7();
    // get uniform dist from 1 - 63
    idx = b + (a-1)*7;
    if (idx <= 60)
      return 1 + (idx-1)%10;
    a = idx-60;
    b = rand7();
    // get uniform dist from 1-21
    idx = b + (a-1)*7;
    if (idx <= 20)
      return 1 + (idx-1)%10;
  }
}
The expected value for the number of calls to rand7() function using this optimization is: