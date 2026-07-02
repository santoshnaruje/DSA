from typing import List


class Solution:

    def mergeOverlappingIntervalsBruteForce(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []
        n = len(intervals)
        intervals.sort()
        i = 0
        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]
            j = i + 1
            while j < n and intervals[j][0] <= end:
                end = max(end, intervals[j][1])
                j += 1
            merged_intervals.append([start, end])
            i = j
        return merged_intervals

    def mergeOverlappingIntervalsOptimal(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = []
        for start, end in intervals:
            if not merged_intervals or merged_intervals[-1][1] < start:
                merged_intervals.append([start, end])
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], end)

        return merged_intervals

if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    solution = Solution()
    result = solution.mergeOverlappingIntervalsOptimal(intervals)
    print(result)
