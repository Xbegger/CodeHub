/*
 * @lc app=leetcode.cn id=222 lang=java
 *
 * [222] 完全二叉树的节点个数
 */

// @lc code=start
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
    public int countNodes(TreeNode root) {
        if(root == null){
            return 0;
        }
        TreeNode l = root, r = root;

        int hl = 0, hr = 0;

        while(l != null){
            l = l.left;
            hl = hl + 1;
        }

        while(r != null){
            r = r.right;
            hr = hr + 1;
        }
        if(hl == hr){
            return (int)Math.pow(2, hl) - 1;
        }

        return 1 + countNodes(root.left) + countNodes(root.right);
    }
}
// @lc code=end

