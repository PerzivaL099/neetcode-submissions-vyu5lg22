class Solution {
    public int climbStairs(int n) {
        //edge case
        if (n <= 2)
            return n;

        //Initialize both possible operations
        int n1 = 1, n2 = 2;

        //Iterate through 
        for (int i = 3; i <= n; i++){
            int current = n1+n2;
            n1 = n2;
            n2 = current;
        }

        return n2;
    }
}
