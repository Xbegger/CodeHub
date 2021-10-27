/*
 * @lc app=leetcode.cn id=1373 lang=java
 *
 * [1373] 二叉搜索子树的最大键值和
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
    int max = 0;
    public int maxSumBST(TreeNode root) {
        maxSumSubBST(root);
        
        return max;
    }
    int maxSumSubBST(TreeNode root){
        if(root == null){
            return 0;
        }
        int left, right;
        left = maxSumBST(root.left);
        right = maxSumBST(root.right);
        System.out.println("root: " + root.val + "left:" + left + "  right:" + right);
        if(left > max){
            max = left;
        }
        if(right > max){
            max = right;
        }
        
        return (left + right + root.val); 
    }
}
// @lc code=end

