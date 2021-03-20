from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        逆波兰表达式求值: 使用操作数栈存储操作数
        '''
        operand = []
    
        for ele in tokens:
            if ele == '/':
                x = operand.pop()
                y = operand.pop()
                operand.append(int(y/x))
            elif ele == '*':
                x = operand.pop()
                y = operand.pop()
                operand.append(x*y)
            elif ele == '+':
                x = operand.pop()
                y = operand.pop()
                operand.append(x+y)
            elif ele == '-':
                x = operand.pop()
                y = operand.pop()
                operand.append(y-x)
            else:
                operand.append(int(ele))

        return operand[0]

    def middle2suffix(self, tokens: List[str]) -> List[str]:
        '''
        中缀表达式转后缀表达式: 使用操作符栈
        1. 遇到操作数, 输出
        2. 遇到 (、*、/三个操作符直接加入操作数栈
        3. 遇到)
            3.1 依次弹出operator中的栈顶元素并依次输出,直到栈顶元素是(为止. (注意: '('不输出)
        4. 遇到 +、-
            4.1 若当前栈顶元素是*、/, 则 依次弹出栈顶元素并输出, 然后将当前符号入栈
            4.2 若当前栈顶元素是+、-, 则入栈
        '''
        # result = []
        operator = []
        for ele in tokens:
            if ele > "0" and ele <= "9":
                # 如果当前元素是操作数,则直接输出
                print(ele, end='')
            elif ele == '+' or ele == '-':
                # 如果当前元素是+
                if len(operator) == 0:
                    # 如果当前操作符栈为空,则将当前元素加入栈中
                    operator.append(ele)
                elif operator[-1] == '*' or operator[-1] == '/':
                    # 栈顶操作符 > 当前元素符号
                    while len(operator):
                        top = operator.pop()
                        print(top, end='')
                elif operator[-1] == '+' or operator[-1] == '-':
                    # 栈顶操作符 > 当前元素符号
                    operator.append(ele)
                elif operator[-1] == '(':
                    operator.append(ele)
                else:
                    print('异常的元素')
            elif ele == '/' or ele == '*':
                operator.append(ele)

            elif ele == '(':
                operator.append(ele)
            elif ele == ')':
                # 找到对应的(
                while len(operator) > 0:
                    top = operator.pop()
                    if(top == '('):
                        break
                    else:
                        print(top, end='')
        else:
            while len(operator):
                top = operator.pop()
                print(top, end='')

    def middle2prefix(self, tokens: List[str]) -> List[str]:
        '''
        中缀表达式转前缀表达式
        '''
        pass


# 1+(2-3)*4+10/5
# 123-+

tokens = ["4", "3", "-"]
# 转为中序表达式为: ((2 + 1) * 3)
solution = Solution()
print(solution.evalRPN(tokens))
# solution.middle2suffix(
#     ['1', '+', '(', '2', '-', '3', ')', '*', '4', '+', '12', '/', '5'])


# a + b * (c - d) + e/f
#          *b-cd/ef
