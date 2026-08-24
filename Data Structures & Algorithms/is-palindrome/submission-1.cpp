class Solution {
public:
    bool isPalindrome(string s) {
        // Create empy string 
        std::string cleanStr = "";

        // Loop through each character in input string
        for (char c : s) {
            if (isalnum(c)) {
                cleanStr += tolower(c);

            }
        }

        // Return if the new string and its reverse is equal
        return cleanStr == string(cleanStr.rbegin(), cleanStr.rend());

    }
};
