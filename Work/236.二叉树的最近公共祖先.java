/*
 * @lc app=leetcode.cn id=236 lang=java
 *
 * [236] 二叉树的最近公共祖先
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return traverse(root, p, q);
    }
    TreeNode traverse(TreeNode root, TreeNode p, TreeNode q){
        TreeNode left, right;
        if(root == null){
            return null;
        }
        if(root == p || root == q){
            return root;
        }


        left = traverse(root.left, p, q);
        right = traverse(root.right, p, q);
        
        // 后序遍历p, q两节点第一次相交的地方就是最近的公共祖先

        // case 1: p, q 都在以root为根的子树
        if(left != null && right != null){
            return root;
        }
        // case 2: p, q 都不在以root为根的子树
        if(left == null && right == null){
            return null;
        }
        // case 3: p, q 只有一个在以root为根的子树
        return left == null ? right : left;
    }
}
// @lc code=end

