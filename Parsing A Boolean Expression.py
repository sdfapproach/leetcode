# https://leetcode.com/problems/parsing-a-boolean-expression/?envType=daily-question&envId=2024-10-20
# Parsing A Boolean Expression

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        def calc(operator, bool_list):

            boolean = None

            if operator == "!":
                if bool_list[0] == True:
                    return False
                else:
                    return True

            elif operator == "&":

                for b in bool_list:
                    if boolean is None:
                        boolean = b
                    else:
                        boolean &= b

            elif operator == "|":
                for b in bool_list:
                    if boolean is None:
                        boolean = b
                    else:
                        boolean |= b

            return boolean
        
        stack = []

        for item in expression:

            if item == ")":
                bool_list = []

                while stack[-1] != "(":

                    bool_list.append(stack.pop())
                
                stack.pop()
                operator = stack.pop()

                stack.append(calc(operator, bool_list))
            else:
                if item == "t":
                    stack.append(True)
                elif item == "f":
                    stack.append(False)
                elif item == ",":
                    continue
                else:
                    stack.append(item)

        return stack.pop()