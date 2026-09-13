class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Bucket sort
        // Frequency map
        unordered_map<int, int> count;
        for (int n: nums) {
            count[n]++;
            
        }

        // 2. Bucket[i] = list of numbers that appear exactly i times
        vector<vector<int>> bucket(nums.size() + 1);
        for (auto& [num, f] : count) {
            bucket[f].push_back(num);
        }

        // 3. Scan from highest frequency downward
        vector<int> res;
        for (int i = bucket.size() - 1; i >= 1 && res.size() < k; --i) {
            for (int num : bucket[i]) {
                res.push_back(num);
                if (res.size() == k) break;
            }
        }
        return res;

    }
};
