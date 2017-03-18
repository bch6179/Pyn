1. null or empty string
2. white spaces
3. +/- sign
4. calculate real value
5. handle min & max
Java Solution

public int atoi(String str) {
    if (str == null || str.length() < 1)
        return 0;

    // trim white spaces
    str = str.trim();

    char flag = '+';

    // check negative or positive
    int i = 0;
    if (str.charAt(0) == '-') {
        flag = '-';
        i++;
    } else if (str.charAt(0) == '+') {
        i++;
    }
    // use double to store result
    double result = 0;

    // calculate value
    while (str.length() > i && str.charAt(i) >= '0' && str.charAt(i) <= '9') {
        result = result * 10 + (str.charAt(i) - '0');
        i++;
    }

    if (flag == '-')
        result = -result;

    // handle max and min
    if (result > Integer.MAX_VALUE)
        return Integer.MAX_VALUE;

    if (result < Integer.MIN_VALUE)
        return Integer.MIN_VALUE;

    return (int) result;
}

//    if (num > Integer.MAX_VALUE / 10 ||
//                 num == Integer.MAX_VALUE / 10 &&
//                 num > Integer.MAX_VALUE % 10) {
//                 return negFlag ? Integer.MAX_VALUE : Integer.MIN_VALUE;
//             }
public static final int MAX_DIGITS = 10;
String IntegerToString(int num) {

    char[] temp = new char(MAX_DIGITS + 1);
    int i = 0;
    boolean sign = false;
    if (num < 0)  {
        sign = true;
        num = -num;
    }
    do{
        temp[i++] = (char) (num % 10 + '0');
        num /= 10;
    }while(num = 0);

    StringBuilder b = new StringBuilder();

    if (sign) b.append('-');

    while(i > 0) {
        b.append(temp[--i]);
    }

    return b.toString();
}