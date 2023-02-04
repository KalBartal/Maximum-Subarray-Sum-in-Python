def maxSubarraySum(arr):
    # create a list to store the maximum sum of all subarrays from the
    # beginning of the array to the current position
    subarrays_sum = [0]
    # variable to keep track of the maximum sum of all subarrays seen so far
    max_sum = 0

    # loop through the array and calculate the maximum sum of the subarray
    # starting at the beginning, and add the
    # current element to it
    for num in arr:
        subarrays_sum.append(max(subarrays_sum[-1] + num, num))
        max_sum = max(max_sum, subarrays_sum[-1])

    # return the maximum sum of all subarrays
    return max_sum


# For example, given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4], the maximum
# sum is 6 because the subarray [4, -1, 2,
# 1] has the largest sum.
print(maxSubarraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
