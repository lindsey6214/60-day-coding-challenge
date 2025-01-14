class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

'''
Time complexity: The one-pass approach achieves a time complexity of O(n), where n is the size of the input array nums. This is the best possible time complexity for this problem, as any solution needs to examine all elements in the array at least once to determine the pair that sums up to the target.
Space complexity: The space used by the algorithm primarily comes from the dictionary (or hashmap) used to store the seen elements and their indices during the scan. In the worst-case scenario, when all elements in the array are unique, the dictionary could store n elements, leading to O(n) space complexity.
'''
