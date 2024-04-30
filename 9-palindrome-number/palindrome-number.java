import java.util.*;

class Solution {
    public boolean isPalindrome(int x) {
        String numberString = Integer.toString(x);
        char[] number = numberString.toCharArray();
        int start = 0;
        int end = number.length - 1;

        while(end > start) {
            if(number[start] != number[end]) {
                return false;
            }
            end--;
            start++;
        }
        return true;
    }
}