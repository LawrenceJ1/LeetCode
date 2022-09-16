class Solution {
    HashMap<Integer, Integer> ans = new HashMap<Integer, Integer>();
    
    public int majorityElement(int[] nums) {
        for (int num: nums) {
            if (!ans.containsKey(num)) {
                ans.put(num, 1);
            } else {
                ans.put(num, ans.get(num)+1);
            }
        }
        for (int key: ans.keySet()) {
            if (ans.get(key) > Math.floor(nums.length/2)) {
                return key;
            }
        }
        return 0;
    }
}