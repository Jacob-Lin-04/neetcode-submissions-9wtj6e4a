class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // Map the 1D index to the 2D Rows and Columns
        int rows = matrix.size();
        int cols = matrix[0].size();
        int totalElements = rows * cols;

        // Binary Search
        int left = 0, right = totalElements - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if ((matrix[mid / cols][mid % cols]) == target){
                return true;

            }

            if (matrix[mid / cols][mid % cols] < target) {
                left = mid + 1;

            }

            else {
                right = mid - 1;

            }

        }
        // does not exist 
        return false;
        
    }
};
