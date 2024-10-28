class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]  # Convert to 1-based indexing
            elif current_sum < target:
                left += 1  # Move left pointer to the right
            else:
                right -= 1  # Move right pointer to the left
        
        return []  # In practice, this line should never be reached since the problem guarantees a solution

# Example usage:
# sol = Solution()
# print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]
# print(sol.twoSum([2, 3, 4], 6))       # Output: [1, 3]
# print(sol.twoSum([-1, 0], -1))        # Output: [1, 2]
