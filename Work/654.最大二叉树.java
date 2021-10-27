/*
 * @lc app=leetcode.cn id=654 lang=java
 *
 * [654] 最大二叉树
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
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return constructTree( nums, 0, nums.length);
    }
    public TreeNode constructTree(int[] nums, int left, int right){
        if(left >= right){
            return null;
        }
        int maxNo = left;

        for(int i=left; i<right; i++){
            if(nums[i] > nums[maxNo]){
                maxNo = i;
            }
        }
        TreeNode root = new TreeNode(nums[maxNo]);
        root.left = constructTree(nums, left, maxNo);
        root.right = constructTree(nums, maxNo+1, right);
        return root;
    }
}
// @lc code=end

