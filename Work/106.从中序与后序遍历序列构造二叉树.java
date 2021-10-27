/*
 * @lc app=leetcode.cn id=106 lang=java
 *
 * [106] 从中序与后序遍历序列构造二叉树
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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        return build(inorder, 0, inorder.length, postorder, postorder.length - 1);
    }

    TreeNode build(int[] inorder, int left, int right, int[] postorder, int k){
        if(left >= right){
            return null;
        }
        int rootNo = left;
        int nextK = k;
        for(int i = right - 1; i >= left ; i--){
            nextK = nextK - 1;
            if(inorder[i] == postorder[k]){
                rootNo = i;
                break;
            }
        }
        TreeNode root = new TreeNode(postorder[k]);
        root.left = build(inorder, left, rootNo, postorder, nextK);
        root.right = build(inorder, rootNo + 1, right, postorder, k - 1);

        return root;
    }
}
// @lc code=end

