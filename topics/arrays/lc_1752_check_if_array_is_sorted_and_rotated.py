"""
Title: Check if Array Is Sorted and Rotated
Source: LeetCode (LC-1752)
Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
Topic: Arrays
Tags: array, rotation, invariant
Difficulty: Easy

Key idea:
Count the number of "drops" where the sequence decreases: nums[i] > nums[i+1].
A non-decreasing array rotated any number of times can have at most one such drop
(the rotation pivot). Use circular indexing to include the last->first comparison.

Why it works (correctness sketch):
If nums is a rotation of a non-decreasing array, the order is non-decreasing everywhere
except possibly at the pivot where the largest element is followed by the smallest,
creating exactly one decrease (or zero decreases if not rotated / all equal).
If there are two or more decreases, no single rotation can make the array globally
non-decreasing.

Complexity:
Time: O(n)
Space: O(1)

Notes:
- Handles duplicates naturally because equality is allowed (non-decreasing).
- Circular check via (i + 1) % n ensures the last-to-first boundary is validated.
"""

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        drops = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drops += 1
                if drops > 1:
                    return False

        return True
