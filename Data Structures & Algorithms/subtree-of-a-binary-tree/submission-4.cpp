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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        // Recursion base case
        if (root == nullptr) {
            return false;
        }

        if (isSameTree(root, subRoot)) {
            return true;

        } else {
            return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);

        }

        
    }
    
    // Function to check if two trees are exactly the same
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == nullptr && q == nullptr) {
            return true;
        }

        if (p == nullptr || q == nullptr || p->val != q->val) {
            return false;
        }

        if (p->val == q->val) {
            bool left = isSameTree(p->left, q->left);
            bool right = isSameTree(p->right, q->right);

            return left and right;
        }

     }
};
