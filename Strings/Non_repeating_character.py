"""
Link:
https://www.geeksforgeeks.org/problems/non-repeating-character-1587115620/1?page=1&category=Strings&sortBy=submissions

Given a string S consisting of lowercase Latin Letters. Return the first non-repeating character in S. If there is no non-repeating character, return '$'.

Example 1:

Input:
S = hello
Output: h
Explanation: In the given string, the
first character which is non-repeating
is h, as it appears first and there is
no other 'h' in the string.
Example 2:

Input:
S = zxvczbtxyzvy
Output: c
Explanation: In the given string, 'c' is
the character which is non-repeating. 
Your Task:
You only need to complete the function nonrepeatingCharacter() that takes string S as a parameter and returns the character. If there is no non-repeating character then return '$' .

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Number of distinct characters).
Note: N = |S|

Constraints:
1 <= N <= 10^5

"""

class Solution:
    def nonrepeatingCharacter(self,s):
        dictionary={}
        n=len(s)
        for i in range(0,n):
            if s[i] in dictionary:
                dictionary[s[i]]=dictionary[s[i]]+1
            else:
                dictionary[s[i]]=1
        for i in range(0,n):
            if(dictionary[s[i]]==1):
                return s[i]
        return "$"
