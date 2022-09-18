class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        int count=0, left=-1, right=-1;
        Arrays.sort(intervals, (x, y) -> x[0] - y[0]);
        for (int[] e: intervals) {
            if (e[0] > left && e[1] > right) {
                count++;
                left = e[0];
            }
            right = Math.max(right, e[1]);
        }
        return count;
    }
}