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
class BSTIterator {
    List<Integer> bst;
    int counter;
    
    public BSTIterator(TreeNode root) {
        bst = new ArrayList<>();
        counter = -1;
        traverse(root);
    }
    
    public int next() {
        return bst.get(++counter);
    }
    
    public boolean hasNext() {
        return counter+1 < bst.size();
    }
    
    private void traverse(TreeNode node) {
        if (node == null) 
            return;
        traverse(node.left);
        bst.add(node.val);
        traverse(node.right);
    } 
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */