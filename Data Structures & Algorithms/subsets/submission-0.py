class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def dfs(index: int) -> None:
            # Every decision has been made
            if index == len(nums):
                result.append(current.copy())
                return

            # Choice 1: include nums[index]
            current.append(nums[index])
            dfs(index + 1)

            # Undo the choice
            current.pop()

            # Choice 2: exclude nums[index]
            dfs(index + 1)

        dfs(0)
        return result