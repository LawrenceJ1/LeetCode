class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        List<Integer> left = new ArrayList<Integer>();
        return dfs(root, 0, 0, left);        
    }
    private int dfs(TreeNode node, int depth, int pos, List<Integer> left) {
        if (node == null) return 0;
        if (left.size() == depth) left.add(pos);
        return Math.max(1+pos-left.get(depth), Math.max(dfs(node.left, depth+1, pos*2, left), dfs(node.right, depth+1, 1+pos*2, left)));
    }
}