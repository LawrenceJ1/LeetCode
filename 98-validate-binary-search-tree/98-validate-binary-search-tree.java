/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        return helper(root, Long.MAX_VALUE, Long.MIN_VALUE);
    }
    private boolean helper(TreeNode root, long max, long min) {
        if (root == null) 
            return true;
        if (root.val <= min || root.val >= max)
            return false;
        return (helper(root.left, root.val, min) && helper(root.right, max, root.val));
    }
}