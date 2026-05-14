class Solution {
    public int longestConsecutive(int[] nums) {
        //Define hashmap & maxLength
        Set<Integer> numSet = new HashSet<>();
        //Add all values to hashSet
        for (int num: nums){
            numSet.add(num);
        }

        int numLength = 0;

        //Iterate through hashmap
        for (int n: numSet){
            if (!numSet.contains(n-1)){
                int length = 1;
                while (numSet.contains(n + length)){
                    length++;
                }
                numLength = Math.max(numLength, length);
            }
        }
        return numLength;
        
    }
}
