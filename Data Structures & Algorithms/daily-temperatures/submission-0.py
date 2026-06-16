class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        indicies = []
         
        #loop through once
        for i, temp in enumerate(temperatures):
            
            #if there are items in indicies and if current temp is
            #warmer than the index at the top of the stack
            while indicies and temp > temperatures[indicies[-1]]:
                prev_index = indicies.pop()
                results[prev_index] = i - prev_index

            #push current index onto stack to find its warmer day later
            indicies.append(i)
            
        return results




        