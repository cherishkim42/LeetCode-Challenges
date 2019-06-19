"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
"""

class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)