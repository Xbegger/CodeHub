/*
 * @lc app=leetcode.cn id=96 lang=java
 *
 * [96] 不同的二叉搜索树
 */

// @lc code=start
class Solution {
    public int numTrees(int n) {
        memo = new int[n][n];
        return count(0, n-1);
    }
    int[][] memo;
    int count(int left, int right){
        if(left >= right){
            return 1;
        }
        if(memo[left][right] != 0){
            return memo[left][right];
        }
        int leftCnt, rightCnt;
        int ans = 0;
        for(int i=left; i<=right; i++){
            leftCnt = count(left, i - 1);
            rightCnt = count(i + 1, right);
            ans = ans + leftCnt * rightCnt;
        }
        memo[left][right] = ans;
        return ans;
    }
}
// @lc code=end

