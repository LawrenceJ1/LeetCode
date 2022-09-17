class Solution {
    public String removeKdigits(String num, int k) {
        Deque<Character> nums = new ArrayDeque<>();
        int count = 0;
        for(int i = 0; i < num.length(); i++) {
            while ((nums.size() > 0) && ((int)nums.getLast() > (int)num.charAt(i)) && (count < k)) {
                nums.removeLast();
                count++;
            }
            nums.addLast(num.charAt(i));
        }
        for(int i=count; i<k; i++) {
            nums.removeLast();
        }
        while ((nums.size() > 0) && (nums.getFirst() == '0')) {
            nums.removeFirst();
        }
        if (nums.size() == 0) {
            return "0";
        }
        StringBuilder sb = new StringBuilder();
        while(nums.size() > 0)
            sb.append(nums.removeFirst());
        return sb.toString();
    }
}