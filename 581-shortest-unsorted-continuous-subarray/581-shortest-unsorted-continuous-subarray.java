class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        boolean flag = false;
        for(int i = 0; i < nums.length-1; i++) {
            if (nums[i] > nums[i+1]) {
                flag = true;
            }
            if (flag) {
                min = Math.min(min, nums[i+1]);   
            }            
        }
        flag = false;
        for(int i = nums.length-1; i > 0; i--) {
            if (nums[i] < nums[i-1]) {
                flag = true;
            }
            if (flag) {
                max = Math.max(max, nums[i-1]);
            }
        }
        int start, end;
        for(start = 0; start < nums.length; start++) {
            if (nums[start] > min) {
                break;
            }
        }
        for(end = nums.length-1; end >= 0; end--) {
            if (nums[end] < max) {
                break;
            }
        }
        return end-start < 0 ? 0 : end-start+1;
    }
}