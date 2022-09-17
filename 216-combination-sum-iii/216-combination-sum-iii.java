class Solution {
    int total;
    ArrayList ans = new ArrayList<ArrayList<Integer>>();
    public List<List<Integer>> combinationSum3(int k, int n) {
        total = n;
        dp(k, new ArrayList<>(), 1);
        return ans;
    }
    private void dp(int left, ArrayList<Integer> nums, int start) {
        if(left == 0 && nums.stream().mapToInt(Integer::intValue).sum() == total) {
            ans.add(new ArrayList<Integer>(nums));
        } else {
            if(left != 0) {
                left--;
                for(int i = start; i < 10-left; i++) {
                    nums.add(i);
                    dp(left, nums, i+1);
                    nums.remove(nums.size()-1);
                }
            }
        }
    }
}