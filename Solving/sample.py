class Solution(object):
    def romanToInt(self, s):
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        r=0
        for n in range(len(s)):
            if roman[s[n]] <roman[s[n]]+1 and roman[s[n]] < len(s):
                r-=roman[s[n]]
        else:
            r+=roman[s[n]]
        return r
s="IX"
s2=Solution()
print(s2.romanToInt(s))