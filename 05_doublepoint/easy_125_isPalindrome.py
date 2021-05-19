class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        题目: 验证回文串,给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
        '''
        l, r = 0, len(s)-1
        while l <= r:
            # 过滤左指针的非字母和数字
            if ord(s[l]) < 48 or 57 < ord(s[l]) < 65 or 90 < ord(s[l]) < 97 or ord(s[l]) > 122:
                l += 1
                continue
            # 过滤右指针的非字母和数字
            if ord(s[r]) < 48 or 57 < ord(s[r]) < 65 or 90 < ord(s[r]) < 97 or ord(s[r]) > 122:
                r -= 1
                continue
            # 左右指针都是数字并且相等
            if 48 <= ord(s[l]) <= 57 and s[l] != s[r]:
                return False
            # 左右指针, 左边字母, 右边数字
            elif 65 <= ord(s[l]) <= 122 and 48 <= ord(s[r]) <= 57:
                return False
            elif 65 <= ord(s[l]) <= 122 and (ord(s[l]) != ord(s[r]) and abs(ord(s[l])-ord(s[r])) != 32):
                return False
            l += 1
            r -= 1
            "".isalnum()
        return True


# 48   57  65  90   97  122
# 0    9   A   Z    a   z
s = Solution()
print('res', s.isPalindrome("ab_a"))
