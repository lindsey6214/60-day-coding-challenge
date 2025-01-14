class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

'''
Time complexity: O(n), where n is the size of the input array nums. The first two loops that count the frequency and populate the freq list both run in O(n) time. The last loop iterates through freq in reverse order and adds elements to the res list, which takes O(n) time as well. Thus, the overall time complexity is O(n).
Space complexity: O(n), as it uses a dictionary count to store the frequency of elements and a list freq to store elements grouped by frequency. The res list, which stores the k most frequent elements, can have at most k elements, but since k is a constant (given as input), the space complexity is dominated by the dictionary and the list
'''
