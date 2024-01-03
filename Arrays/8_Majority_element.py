""" 
Link:
https://www.geeksforgeeks.org/problems/majority-element-1587115620/1?page=1&category=Arrays&sortBy=submissions

Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears strictly more than N/2 times in the array.
 

Example 1:

Input:
N = 3 
A[] = {1,2,3} 
Output:
-1
Explanation:
Since, each element in 
{1,2,3} appears only once so there 
is no majority element.
Example 2:

Input:
N = 5 
A[] = {3,1,3,3,2} 
Output:
3
Explanation:
Since, 3 is present more
than N/2 times, so it is 
the majority element.

Your Task:
The task is to complete the function majorityElement() which returns the majority element in the array. If no majority exists, return -1.
 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 

Constraints:
1 ≤ N ≤ 10^7
0 ≤ Ai ≤ 10^6 
"""

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        count={}
        for i in A:
            if (i in count):
                count[i]+=1
            else:
                count[i]=1
            if(count[i]>N/2):
                return i
        return -1