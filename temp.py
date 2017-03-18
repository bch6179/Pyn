mid = (start + end) / 2;
will have overflow issue when start and end is very large. Imagine if start is 0.5MAX_INT and end is MAX_INT. start + end will be potentially be 1.5MAX_INT which is equivalent to 1011 1111 1111 1111 1111 1111 1111 1110 binary string.
Now if you just use /2 then it will treat the binary string as signed integer (-1073741826) and you mid point will be negative. However, if you logical shift right (Logical right shift, however, does not care that the value could possibly represent a number; it simply moves everything to the right and fills in from the left with 0s) then it is equivalent to dividing by two without caring about the sign.

Alternatively to prevent overflow you can use this expression instead
int mid = start + ((end - start) / 2)
This will ensure no overflow problem exists.

The expression mid = (start + end) / 2 is a quite well known binary search bug. You can read more about it here https://research.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html.