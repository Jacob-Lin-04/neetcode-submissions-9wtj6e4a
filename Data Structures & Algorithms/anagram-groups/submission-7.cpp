class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Hash map where:
        // Key: sorted version of a string (e.g., "act" and "cat" both become "act")
        // Value: vector of all original strings that match this sorted key
        // Anagrams have the same characters, so they'll have identical sorted forms
        unordered_map<string, vector<string>> groups;

        // Vector to store our final result (list of grouped anagrams)
        vector<vector<string>> result;

        // Iterate through each string in the input array
        for (string& s : strs){
            // Create a copy of the current string to use as a key
            string key = s;
            
            // Sort the characters in the key alphabetically. All anagrams will produce the same sorted string
            sort(key.begin(), key.end());
            
            // Add the original string to the group that shares this sorted key
            // If this is the first anagram with this pattern, a new vector is created automatically
            groups[key].push_back(s);
        }

        // Iterate through all groups in the hash map
        for (auto& pair : groups) {
            // Extract the vector of anagrams (pair.second is the value in the key-value pair)
            // and add it to our result
            result.push_back(pair.second);
        }

        return result;
        
    };
};
