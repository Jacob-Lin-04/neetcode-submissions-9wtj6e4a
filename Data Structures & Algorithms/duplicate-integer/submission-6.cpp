class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // No numbers in list
        if (nums.empty()) {
            return false;
        }

        // Solution by sorting array first
        sort(nums.begin(), nums.end());

        // Duplicates will be adjacent
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] == nums [i + 1]) {
                return true;
            }
        }
        
        // No duplicates
        return false;
    };
};