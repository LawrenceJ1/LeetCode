/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode pointer;
        if (head == null || head.next == null) {
            return head;
        }
        pointer = head.next;
        recursive(head);
        return pointer;
    }
    private ListNode recursive(ListNode node) {
        ListNode temp;
        if (node == null) {
            return null;
        }
        if (node.next == null) {
            return node;
        }
        temp = node.next;
        node.next = node.next.next;
        temp.next = node;
        node.next = recursive(node.next);
        return temp;
    }
}