class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_1 = {}
       

        for s in strs:
            string_sorted = "".join(sorted(s))

            if string_sorted not in str_1:
                str_1[string_sorted] = []

            str_1[string_sorted].append(s)

        return list(str_1.values())

        