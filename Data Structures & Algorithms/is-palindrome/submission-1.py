class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=''
        for i in range(len(s)):
            if s[i].isalpha():
                s1+=s[i].lower()
            elif s[i].isdigit():
                s1+=str(i)
        return s1==s1[::-1]

        