class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // Set to remove any duplicate
        std::unordered_set<int> numSet(nums.begin(), nums.end());
        int maxCounts = 0;


        // Loop through each number in set
        for (int n : numSet){
            // Start of sequenc if current numeber -1 is not in set
            if (numSet.find(n -1) == numSet.end()){
                int currentNum = n;
                int currentCount = 1;

                // While the next number in sequence is in the set
                while (numSet.find(currentNum + 1) != numSet.end()){
                    if (currentCount >= maxCounts) {
                        maxCounts = currentCount + 1;

                    }

                    // Increment
                    currentCount += 1;
                    currentNum += 1;
                }
                
                // Update maximum
                maxCounts = max(maxCounts, currentCount);
            }
        }

        return maxCounts; 
    }
};