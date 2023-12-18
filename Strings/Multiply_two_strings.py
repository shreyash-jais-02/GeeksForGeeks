"""
Link:
https://www.geeksforgeeks.org/problems/multiply-two-strings/1?page=1&category=Strings&sortBy=submissions

Given two numbers as strings s1 and s2. Calculate their Product.

Note: The numbers can be negative and You are not allowed to use any built-in function or convert the 
strings to integers. There can be zeros in the begining of the numbers. You don't need to specify '+' 
sign in the begining of positive numbers.


Example 1:

Input:
s1 = "0033"
s2 = "2"
Output:
66


Example 2:

Input:
s1 = "11"
s2 = "23"
Output:
253

Your Task: You don't need to read input or print anything. Your task is to complete the function multiplyStrings() which takes two strings s1 and s2 as input and returns their product as a string.

Expected Time Complexity: O(n1* n2)
Expected Auxiliary Space: O(n1 + n2); where n1 and n2 are sizes of strings s1 and s2 respectively.

Constraints:
1 ≤ length of s1 and s2 ≤ 10^3

"""

#User function Template for python3

class Solution:
    def multiplyStrings(self,s1,s2):
        # initialization
        digits={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        s=[s1,s2]
        n=[len(s1),len(s2)]
        sign=[1,1]
        start=[0,0]
        numbers=[0,0]
        
        # check for minus sign
        for i in range(2):
            if s[i][0]=="-":
                sign[i]=-1
                start[i]=1
        
        # check for zeros
        for i in range(2):
            while start[i]<n[i] and s[i][start[i]]=="0":
                start[i]=start[i]+1
                
        # convert to numbers
        for i in range(2):
            for k in range(start[i],n[i]):
                numbers[i]=numbers[i]*10+digits[s[i][k]]
        
        # calculate the product
        n=sign[0]*sign[1]*numbers[0]*numbers[1]
        
        # convert to string
        if n==0:
            return "0"
        s=""
        inv_dig={v:k for k,v in digits.items()}
        n=abs(n)
        while n!=0:
            d=n%10
            s=s+inv_dig[d]
            n=n//10
        if sign[0]*sign[1]==-1:
            s=s+"-"
        
        return s[::-1]