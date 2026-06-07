// https://leetcode.com/problems/create-binary-tree-from-descriptions/?envType=daily-question&envId=2026-06-07
// Create Binary Tree From Descriptions

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[][]} descriptions
 * @return {TreeNode}
 */
var createBinaryTree = function(descriptions) {
    
    const nodes = new Map();
    const children = new Set();

    for (const [parent, child, isLeft] of descriptions) {
        if (!nodes.has(parent)) {
            nodes.set(parent, new TreeNode(parent));
        }

        if (!nodes.has(child)) {
            nodes.set(child, new TreeNode(child));
        }

        if (isLeft === 1) {
            nodes.get(parent).left = nodes.get(child);
        } else {
            nodes.get(parent).right = nodes.get(child);
        }

        children.add(child);
    }

    let root = null;

    for (const [parent] of descriptions) {
        if (!children.has(parent)) {
            root = nodes.get(parent);
            break;
        }
    }

    return root;

};