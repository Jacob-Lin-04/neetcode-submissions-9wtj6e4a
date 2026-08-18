/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        // Solution using recursive DFS (Post Order)
        int diameter = 0;
        dfs(root, diameter);
        return diameter;
        
    }

    int dfs(TreeNode * root, int& diameter) {
        // Function to return height of subtree at 'root'
        if (!root) return 0;

        // Get height of the left and right subtrees
        int leftHeight = dfs(root->left, diameter);
        int rightHeight = dfs(root->right, diameter);

        // Path through current node = leftHeight + rightHeight
        diameter = max(diameter, leftHeight + rightHeight);

        // Return height of this specific subtree to parent
        return 1 + max(leftHeight, rightHeight);


    }
    
};
