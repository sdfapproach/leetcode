// https://leetcode.com/problems/balance-a-binary-search-tree/?envType=daily-question&envId=2026-02-09
// Balance a Binary Search Tree

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var balanceBST = function(root) {

    function inorderTraversal(node) {
        if (node === null) return [];
        return [
            ...inorderTraversal(node.left),
            node.val,
            ...inorderTraversal(node.right)
        ];
    }

    function sortedArrayToBST(nums) {
        if (nums.length === 0) return null;

        const mid = Math.floor(nums.length / 2);
        const node = new TreeNode(nums[mid]);

        node.left = sortedArrayToBST(nums.slice(0, mid));
        node.right = sortedArrayToBST(nums.slice(mid + 1));

        return node;
    }

    const nums = inorderTraversal(root);
    return sortedArrayToBST(nums);
};