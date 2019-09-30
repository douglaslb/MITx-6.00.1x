# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:19:05 2019

@author: doohl
"""

def isPalindrome(s):
    
    def toChar(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChar(s))

print('')
print('is eve a palindrome?')
print(isPalindrome('eve'))

print('')
print('Is able was I ere I saw Elba a palindrome')
print(isPalindrome('Able was I ere I saw Elba'))


        