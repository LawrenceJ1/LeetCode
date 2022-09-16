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
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode mid = getMid(head);
        ListNode left = sortList(head);
        ListNode right = sortList(mid);
        return mergeSort(left, right);
    }
    private ListNode mergeSort(ListNode node1, ListNode node2) {
        ListNode dummy = new ListNode();
        ListNode pointer = dummy;
        while (node1 != null & node2 != null) {
            if(node1.val < node2.val) {
                pointer.next = node1;
                node1 = node1.next;
            } else {
                pointer.next = node2;
                node2 = node2.next;
            }
            pointer = pointer.next;
        }
        pointer.next = (node1 == null) ? node2 : node1;
        return dummy.next;
    }
    private ListNode getMid(ListNode node) {
        ListNode prev = new ListNode(0, node);
        while (node != null && node.next != null) {
            prev = prev.next;
            node = node.next.next;
        }
        ListNode mid = prev.next;
        prev.next = null;
        return mid;
    }
}