class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area_max = 0 
        stack = []
        heights.append(0) #sentinal 0

        for i, h in enumerate(heights):

            #while current bar is smaller than stack top
            while stack and heights[stack[-1]] > h:
                mid = stack.pop()
                
                #right boundary is iL first bar smaller than bar located at mid
                #left boundary is stack[-1]: closest previous bar smaller than mid
                #handle empty stack
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                #area of rectangle
                area = heights[mid] * width

                if area > area_max:
                    area_max = area

            stack.append(i)
        
        return area_max



        