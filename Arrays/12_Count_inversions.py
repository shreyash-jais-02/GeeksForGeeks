"""
Link:
https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1?page=1&category=Arrays&sortBy=submissions

Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
 

Example 1:

Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 
has three inversions (2, 1), (4, 1), (4, 3).
Example 2:

Input: N = 5
arr[] = {2, 3, 4, 5, 6}
Output: 0
Explanation: As the sequence is already 
sorted so there is no inversion count.
Example 3:

Input: N = 3, arr[] = {10, 10, 10}
Output: 0
Explanation: As all the elements of array 
are same, so there is no inversion count.
Your Task:

You don't need to read input or print anything.
Your task is to complete the function inversionCount() which takes the array arr[] and the size of the array as inputs and returns the inversion count of the given array.

Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 5*10^5
1 ≤ arr[i] ≤ 10^18

"""

class Solution:
    #User function Template for python3

    def merge(self, arr, low, mid, high):
        temp = []
        inv = 0
        left = low
        right = mid + 1
        while left<=mid and right<=high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
                inv += (mid-left+1)

        while left<=mid:
            temp.append(arr[left])
            left+=1
        while right<=high:
            temp.append(arr[right])
            right += 1
        
        for i in range(low, high+1):
            arr[i] = temp[i-low]
        return inv
            
    
    def mergeSort(self,arr, low, high):
        if low>=high:
            return 0
        mid = low + (high-low)//2
        inv = 0
        inv += self.mergeSort(arr, low, mid)
        inv += self.mergeSort(arr, mid+1, high)
        inv += self.merge(arr, low, mid, high)
        return inv
    
    def inversionCount(self, arr, n):
        # Your Code Here
        # print(arr)
        return self.mergeSort(arr, 0, n-1)
