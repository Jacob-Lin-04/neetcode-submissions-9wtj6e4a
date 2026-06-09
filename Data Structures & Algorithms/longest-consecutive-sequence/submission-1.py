class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #set to remove any duplicates
        num_set = set(nums)
        max_count = 0

        #loop through each number in set
        for n in num_set:

            #start of sequence if current number - 1 is nto in set
            if n - 1 not in num_set:
                curr_num = n
                count = 1

                #while the next number in sequence is in the set
                while curr_num + 1 in num_set:
                    if count >= max_count:
                        max_count = count + 1

                    count += 1
                    curr_num += 1

                max_count = max(max_count, count)
               
        
        return max_count


            

