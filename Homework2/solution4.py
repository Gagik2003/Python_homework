def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        characters = {'(':')', '[':']', '{':'}'}
        stack = []
        for i in s:
            if i in characters.keys():
                stack.append(i)
            elif len(stack) != 0 and i == characters[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
