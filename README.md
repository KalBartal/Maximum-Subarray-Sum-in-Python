# Maximum Subarray Sum In Python

[ ![Maximum Subarray Sum In Python](./image.png)](https://youtu.be/lN3iypqu-zI)

This repository contains a solution to the Maximum Subarray Sum Problem in Python. The problem is all about finding the maximum sum of a continuous sequence of numbers within an array. 

I also have a video walkthrough of this challenge available on my [YouTube channel](https://youtu.be/lN3iypqu-zI) and [my blog](https://kalbartal.net/maximum-subarray-sum-in-python)

## Problem Statement
Given an array of integers, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

### Example 
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The largest sum of any contiguous subarray is the subarray [4, -1, 2, 1], which has a sum of 6.

## Solution 
This problem can be solved using a dynamic programming approach. We start by creating a list to store the maximum sum of all subarrays from the beginning of the array to the current position. We also need a variable to keep track of the maximum sum of all subarrays seen so far. 

We then loop through the array, and for each element, we calculate the maximum sum of the subarray starting at the beginning, and add the current element to it. We then compare this maximum sum to the maximum sum of all subarrays seen so far and update the maximum sum if necessary. Once we have gone through the entire array, we will have the maximum sum of all subarrays, which we can then return.

## Time and Space Complexity 
The time complexity of this code is O(n), where n is the length of the array. This is because we loop through the array once and for each element, we calculate the maximum sum of the subarray starting at the beginning and add the current element to it. The comparison and update of the maximum sum is a constant time operation, so the time complexity of this algorithm is linear. 

The space complexity of this code is O(n), where n is the length of the array. This is because we need to store the maximum sum of all subarrays from the beginning of the array to the current position. We are using a list to do this, and the size of the list is equal to the length of the array. Thus, the space complexity is linear. 

## Usage 
To run this code, you need to have Python 3 installed. To execute the code, run the `main.py` file.
