class Solution {
    ArrayList<ArrayList<Integer>> ans = new ArrayList<>();
    private void solve(int sum, int target, int index, int size, int[] candidates, List<Integer> temp){
        if (sum == target) {
            ans.add(new ArrayList<> (temp));
            return;
        }
        if (sum > target) {
            return;
        }
        for (int i=index; i<size; i++) {
            temp.add(candidates[i]);
            solve(sum+candidates[i], target, i, size, candidates, temp);
            temp.remove(temp.size()-1);
        }
    }
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        solve(0, target, 0, candidates.length, candidates, new ArrayList<Integer>());
        return (List)ans;
    }
}