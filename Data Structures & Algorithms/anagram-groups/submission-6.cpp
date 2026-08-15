class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Hash map to store sorted strings
        unordered_map<string, vector<string>> groups;

        // Results list
        vector<vector<string>> result;

        for (string& s : strs){
            string key = s;
            sort(key.begin(), key.end());
            groups[key].push_back(s);

        }

        for (auto& pair : groups) {
            result.push_back(pair.second);

        }

        return result;

    };
};
