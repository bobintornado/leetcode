class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index, num in enumerate(nums):
            if num in dict:
                dict[num] = dict[num] + [index]
            else:
                dict[num] = [index]

        for num, indexes in dict.iteritems():
            if (target - num) in dict:
                # duplicated
                if (target - num) == num:
                    return indexes
                else:
                    return [indexes[0], dict[target - num][0]]
