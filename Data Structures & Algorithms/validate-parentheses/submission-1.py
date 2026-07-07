class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(",
                "}":"{",
                "]":"["}

        stack = []

        for char in s:
            if char in pairs:
                top = stack.pop() if stack else "#"
                    
                if pairs[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack


     
        
        

        