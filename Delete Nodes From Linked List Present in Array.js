// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/?envType=daily-question&envId=2025-11-01
// Delete Nodes From Linked List Present in Array

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {number[]} nums
 * @param {ListNode} head
 * @return {ListNode}
 */
var modifiedList = function(nums, head) {

    const removeSet = new Set(nums);
    const dummy = new ListNode(0, head);
    let curr = dummy;

    while (curr.next) {
        if (removeSet.has(curr.next.val)) {
        curr.next = curr.next.next;
        } else {
        curr = curr.next;
        }
    }

    return dummy.next;
};