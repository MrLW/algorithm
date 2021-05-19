class Solution:
    def isValid(self, s: str) -> bool:
        '''
        题目(有效的括号): 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
                        有效字符串需满足：
                        左括号必须用相同类型的右括号闭合。
                        左括号必须以正确的顺序闭合。

        '''
        table = {
            '(': 'g1',
            ')': 'g1',
            '[': 'g2',
            ']': 'g2',
            '{': 'g3',
            '}': 'g3'
        }
        stack = list()
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif len(stack) == 0 or table[s[i]] != table[stack.pop()]:
                return False
        return len(stack) == 0


s = Solution()
ss = '([}])'
print('res: ', s.isValid(ss))
