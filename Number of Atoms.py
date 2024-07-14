# https://leetcode.com/problems/number-of-atoms/?envType=daily-question&envId=2024-07-14
# Number of Atoms

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        def parse():
            n = len(formula)
            i = 0
            
            def parseElement():
                nonlocal i
                i0 = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                return formula[i0:i]
            
            def parseCount():
                nonlocal i
                if i == n or not formula[i].isdigit():
                    return 1
                i0 = i
                while i < n and formula[i].isdigit():
                    i += 1
                return int(formula[i0:i])
            
            stack = [collections.Counter()]

            while i < n:
                if formula[i] == '(':
                    i += 1
                    stack.append(collections.Counter())
                elif formula[i] == ')':
                    i += 1
                    count = parseCount()
                    top = stack.pop()
                    for k in top:
                        stack[-1][k] += top[k] * count
                else:
                    elem = parseElement()
                    count = parseCount()
                    stack[-1][elem] += count
            
            return stack[0]
        
        counter = parse()
        result = []

        for elem in sorted(counter):

            result.append(elem)
            count = counter[elem]

            if count > 1:
                result.append(str(count))

        return ''.join(result)