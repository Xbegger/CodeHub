/*
 * @lc app=leetcode.cn id=95 lang=java
 *
 * [95] 不同的二叉搜索树 II
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
    public List<TreeNode> generateTrees(int n) {
        // if(n == 0){
        //     return new List<>();
        // }
        return build(1, n);
    }
    List<TreeNode> build(int left, int right){
        List<TreeNode> ans = new LinkedList<>();
        if(left > right){
            ans.add(null);
            return ans;
        }

        for(int i=left; i<=right; i++){
            List<TreeNode> leftTree = build(left, i - 1);
            List<TreeNode> rightTree = build(i + 1, right);

            for(TreeNode lNode : leftTree){
                for(TreeNode rNode : rightTree){
                    TreeNode root = new TreeNode(i);
                    root.left = lNode;
                    root.right = rNode;

                    ans.add(root);
                }
            }
        }

        return ans;
    }
}
// @lc code=end

