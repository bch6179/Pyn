def hp(n, l2r):
    if n == 1: 
        print(1)
        return 1
    print(n)
    if l2r:
        res = 2*hp(n//2, False)
    else:
        res = 2*hp(n//2, True) -1 + n%2   # n = 8, look at this, the last <-  1, 3 , in order to recover 3,2*2-1 ,  
    print(("-->" if l2r else "<--") + " n "+str(n)+ " res "+str(res))
    return res
# 1
# --> n 2 res 2     base = 2
# <-- n 4 res 3  MEANS If n ==4 and <-- , the final result remains 3, which 2*2 - 1
# --> n 8 res 6
# 6
def hp1(n):  # bad , bottom up losing the info of right to left
    base =1
    res = 1
    while 2*base <= n:
        res += base
        if base*2 > n: break
        #if ((n / base) % 2 == 0 and right to left): res -= 1
        base *= 2
    return res
print hp1(8)
# print hp(8, True)
# print hp(4, False)
# public:
#     int lastRemaining(int n) {
#         int base = 1, res = 1;
#         while (base * 2 <= n) {
#             res += base;
#             base *= 2;
#             if (base * 2 > n) break;
#             if ((n / base) % 2 == 1) res += base;
#             base *= 2;
#         }
#         return res;
#     }