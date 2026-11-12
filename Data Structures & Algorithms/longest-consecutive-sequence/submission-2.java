class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set =new HashSet<>();

        int count =0;
        int maxCount =0;
        for(int i =0;i<nums.length;i++){
            set.add(nums[i]);
        }

        for(int i =0;i< nums.length;i++){
            int cur = nums[i];
            while(set.contains(cur-1)){
                set.remove(cur-1);
                count++;
                cur--;
            }
            cur = nums[i];
            while(set.contains(cur+1)){
                set.remove(cur+1);
                count++;
                cur++;
            }
            count++;
            set.remove(nums[i]);
            maxCount = Math.max(maxCount, count);
            count =0;
        }
        return maxCount;
    }

}
