"""
Title: Two Sum
Source: LeetCode (LC-1)
Link: https://leetcode.com/problems/two-sum/description/
Topic: Arrays, Hash Map
Difficulty: Medium

Key idea:
Maintain a hash map of previously seen values -> their indices. While scanning the array,
for each value n at index i, check whether the required complement (target - n) has already
been seen. If yes, return the stored index and i.

Why it works (correctness sketch):
At index i, the map contains only values from earlier indices (< i). If (target - n) exists
in the map, then nums[prevhash[target - n]] + n == target, producing a valid pair without
reusing the same element.

Complexity:
Time: O(n) average, assuming O(1) average-time dict lookups
Space: O(n) for the hash map

Notes:
- Handles duplicates correctly because the complement check is performed before inserting
  the current value (e.g., nums=[3,3], target=6).
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevhash = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevhash:
                return [prevhash[diff], i]

            prevhash[n] = i
        return
        