/*
 * @lc app=leetcode.cn id=114 lang=java
 *
 * [114] 二叉树展开为链表
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

    TreeNode dummpyRoot = new TreeNode(-1);
    TreeNode pre = null;
    public void flatten(TreeNode root){
        if(root == null){
            return ;
        }
        flatten(root.right);
        flatten(root.left);

        root.right = pre;
        root.left = null;
        pre = root;
        
    }
    void flatten2(TreeNode root) {
        if(root == null){
            return ;
        }
        flatten2(root.left);
        flatten2(root.right);
        // 左子树接到root右边
        TreeNode left = root.left;
        TreeNode right = root.right;
        root.left = null;
        root.right = left;
        // 右子树接到左子树最最底下
        TreeNode p = root;
        while(p.right != null){
            p = p.right;
        }
        p.right = right;
    }
    void flatten3(TreeNode root){
        if( root == null ){
            return ;
        }
        TreeNode left = root.left;
        TreeNode right = root.right;
        dummpyRoot.right = root;
        dummpyRoot.left = null;
        dummpyRoot = root;
        flatten3(left);
        flatten3(right);
    }
}
// @lc code=end


​