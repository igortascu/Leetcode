class Solution {
    public int romanToInt(String s) {
        int sum = 0;
        
        char[] chars = s.toCharArray();
        
        for(int i = 0; i < s.length(); i++){
            
            switch(chars[i]){
                case 'M':
                    sum+=1000;
                    break;
                case 'D':
                    sum+=500;
                    break;
                case 'C':
                    sum+=100;
                    break;
                case 'L':
                    sum+=50;
                    break;
                case 'X':
                    sum+=10;
                    break;
                case 'V':
                    sum+=5;
                    break;
                case 'I':
                    sum+=1;
                    break;
            }
            
            if( i != 0 && chars[i-1] == 'I' && (chars[i] == 'V' || chars[i] == 'X')){
                sum-=2;
            }
             if(i != 0 && chars[i-1] == 'X' && (chars[i] == 'L' || chars[i] == 'C')){
                sum-=20;
            }
             if(i != 0 && chars[i-1] == 'C' && (chars[i] == 'D' || chars[i] == 'M')){
                sum-=200;
            }
        }  
        return sum;
    }
}