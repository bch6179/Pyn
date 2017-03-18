
依據以上的討論，我們已經發現了能讓電腦程式猜
對手數字的基礎了。首先在程式中建立一個包含所有
5040 個可能的答案的資料庫。當程式首次猜對方的數
字，並且得到回應之後，就可以依照所得的回應從 5040
個答案中刪除不可能的答案。譬如說，程式首先猜 3194
並且得到 1A2B 的回應時，程式就可以一一檢驗所有的
5040 個可能的答案。從 0123 開始：如果 0123 是答案的
話，那麼程式猜 3194 時，就應該得到 1B 的回應。假設
對手遵守遊戲規則，且不犯錯的情形下，0123 就絕對不
是答案（否則對手必須跟程式講 3194 是 1B）；因此程式
可以將它從現有的可能的答案的資料庫中刪除。程式接
著檢驗 0124：如果 0124 是答案的話，則程式猜 3194 時，
對方應該回應 2A；所以 0124 必定也不是答案，程式因
此可將它自資料庫中清除。接著程式會去檢驗 0125、
0126、0127、0128、0129、0132、0134、0135、0136、
0137 和 0138，並且將它們自可能的答案的資料庫中清
除。當程式檢驗到 0139 時，程式會發現它是一個可能的
答案，因為對 0139 而言，3194 的正確性是 1A2B，所以
程式將 0139 保留在資料庫中。程式就是這樣依序依據對
手的回應檢查所有的可能答案，刪除不可能的候選答
案，保留可能的答案。依據這樣的步驟，程式檢驗過現
有 5040 個可能的答案後，自然會剔除 4824 個已經不可
能是答案的數字，只留下仍可能是答案的 216 個數字。
當下一次輪到程式猜數字時，程式就從這剩下的 216 個
可能的答案中任選一個去猜，然後再重複上述的過程，
依據最近一次所得的回應，再一次篩選和清理資料庫。
如下圖所示，這個程式基本上就是不斷從資料庫中選一
個數字猜測對方答案，然後再依據對手的回應清理可能
科學月刊第三十二卷第三期
圖五 利用篩選法玩猜數字遊戲（假設對手底
牌是 9146）
…,9146,…, 9734,…
0123, 0124, 0125, 0126, 0127, 0128, 0129,
0132, 0134, 0135, 0136, 0137, 0138, 0139,
0142, 0143, 0145, 0146, 0147, 0148, 0149,
5040 個候選答案
因為 3194 是 1A2B
因為 9734 是 1A1B
0123, 0124, 0125, 0126, 0127, 0128, 0129,
0132, 0134, 0135, 0136, 0137, 0138, 0139,
0142, 0143, 0145, 0146, 0147, 0148, 0149,
216 個候選答案
… ,9146,…, 9734, …
… …
0123, 0124, 0125, 0126, 0127, 0128, 0129,
0132, 0134, 0135, 0136, 0137, 0138, 0139,
0142, 0143, 0145, 0146, 0147, 0148, 0149,
40 個候選答案
… ,9146,…, 9734, …
答案的資料庫，直到猜到對方數字為止

u
se trie to save dictionary; use regular expression to search trie to find the possible set; greedy to pick one of the char to find the smallest possible set  based on that.

ask question for what's the most concern worst case or average


求解猜数字游戏的策略通常有两个目标：一是保证在猜测次数限制下赢得游戏，二是使用尽量少的猜测次数。第一个目标追求的是最坏情况下的猜测次数最少，第二个目标追求的是平均情况下猜测次数最少。对于某些数码和数位的规则组合，这两个目标不能同时实现。例如，对于4个数位、6个数码的 Mastermind 游戏，平均猜测次数最少的策略需要平均 4.340 次，但最坏需要6次猜测；如果限制猜测次数最多为5次，则平均猜测次数最少的策略需要平均 4.341 次。[2]
系统的猜测策略可分为三类：简单策略、启发式策略和最优策略。下面以标准规则（10个数码，4个数位，不含重复数字）为例，介绍这几类策略。这些策略也适用于其它规则变体。
这种策略非常直接——每次都猜可能答案中的第一个。例如，首先猜测1234，如果得到的反馈是 2A0B，那么可能的答案包括1256，1257，5236，等等。根据简单策略，下一次就猜1256，因为1256是所有可能答案中最小的数字。
简单策略的优点是速度非常快，缺点是所需猜测次数很多。对于标准规则，简单策略最多需要9次猜测，而平均需要5.560次。
这类策略是猜数字游戏最常用的解法。其算法步骤如下：
a. 首先猜 1234，得到第一个反馈（xAyB）。
b. 从所有数字中，筛选出满足已知反馈的所有可能数字，称之为“可能集”。
c. 对于所有数字（而不仅限于筛选出来的可能集），逐一评估每个数字的“好坏”，并给其打分。选取得分最高的那个数字猜。如果有多个数字的评分一样高，则优先选取可能集中的数字。
d. 重复步骤 b-c，直到猜出 4A0B 为止。
显然，启发式策略的重点在于如何评估一个数字的“好坏”？人们提出了多种直观的评价指标。简介如下：
最坏情况指标(Knuth, 1977)[3]  ：这是最早出现在文献中的策略，在 Mastermind 规则下效果很好。给定一个数字，如果猜这个数字，那么接下来我的“可能集”至少会缩小多少？选取使可能集在最坏情况下最小的那个猜测。对于标准规则，这一评价指标最多需要7次猜测，平均需要 5.385 次。
平均情况指标(Irving, 1978)：这是一个相当直观的指标，在各种规则变体下均有较好的效果。给定一个数字，如果猜这个数字，那么接下来我的“可能集”平均会缩小到多大？选取使可能集的预期大小最小的那个猜测。对于标准规则，这一评价指标最多需要7次猜测，平均需要 5.268 次。
预期步数指标(Neuwirth, 1982)：又称“熵”指标。给定一个数字，这个指标计算如果猜测这个数字，那么接下来估计还需要多少步才能猜到答案。当然，这个步数只是一个粗略的估计，它假设每次猜测可以将可能集缩小一半（或缩小某一个常数倍k），于是估计步数就是可能集大小的对数函数，即估计步数=log(可能集中元素的个数)。对于标准规则，这一评价指标最多需要7次猜测，平均需要 5.265 次。
反馈个数指标(Kooi, 2005)[4]  ：给定一个数字，这个指标计算该数字所可能带来的不同反馈的个数。反馈越多的越好。对于标准规则，这一评价指标最多需要8次猜测，平均需要 5.308 次。
此外，值得注意的是，启发式策略的效果也经常取决于所有数字的排列。不过影响一般不大。
猜数字游戏的最优策略需要由计算机用穷举法获得。其思路是，由于每次猜测的选择是有限的（因为总共的数字组合个数有限），并且我们知道一定可以在有限次数内猜出所有答案，那么计算机可以穷举所有猜法，从中找出最佳的策略。


mport java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class Game {

    public static void main(String[] args) {
        System.out.println("The computer has generate a unique 4 digit number.\n"
                + "You can try to guess the 4 digits number in 5 attempts.\n");
        System.out.println("_______________________________________________________\n");
        int[] random=numberGenerator();
        int maxTry=5;
        int indexMatch=0;
        int match=0;
        while(maxTry>0 && indexMatch!=4){
            int[] guess=getGuess();
            indexMatch=0;
            match=0;
            for(int i=0;i<guess.length;i++){
                if(guess[i]==random[i]){
                    indexMatch++;
                }
                else if(guess[i]==random[0] || guess[i]==random[1] || guess[i]==random[2] || guess[i]==random[3]){
                    match++;
                }
            }
            if(indexMatch==4){
                System.out.print("Well done! Your guess is Correct! The number is: ");
                for(int i=0;i<guess.length;i++){
                    System.out.print(guess[i]);
                }
            }
            else{
                maxTry--;
                if(maxTry>1){
                    System.out.println("You have guess "+indexMatch+" correct number in correct position,"+
                    " and "+match+" correct number in incorrect position. \n"+maxTry+" attempt remaining.");
                }
                else if(maxTry==1){
                    System.out.println("You have guess "+indexMatch+" correct number in correct position,"+
                    " and "+match+" correct number in incorrect position. \nLast attempt!. Good luck");
                }
                else{
                    System.out.println("Sorry, you failed to guess the number in 5 attempts.");
                    System.out.print("The number is: ");
                    for(int i=0;i<random.length;i++){
                        System.out.print(random[i]);
                }
            }
        }
    }
}

public static int[] getGuess(){
    Scanner keyboard = new Scanner(System.in);
    System.out.println("Please enter your guess: ");
    String input = keyboard.nextLine();
        if(input.length()!=4 || input.replaceAll("\\D","").length()!=4){
            System.out.println("Invalid number. You must enter 4 digits between 0-9 only.");
            return getGuess();
    }
    int[] guess = new int[4];
    for (int i = 0; i < 4; i++) {
        guess[i] = Integer.parseInt(String.valueOf(input.charAt(i)));
    }
    return guess;
}

public static int[] numberGenerator() {
    Random randy = new Random();
    int[] randArray = {10,10,10,10};

    for(int i=0;i<randArray.length;i++){
        int temp = randy.nextInt(9);
        while(temp == randArray[0] || temp == randArray[1] || temp == randArray[2] || temp == randArray[3]){
            temp=randy.nextInt(9);
        }
        randArray[i]=temp;
    }
    return randArray;
}