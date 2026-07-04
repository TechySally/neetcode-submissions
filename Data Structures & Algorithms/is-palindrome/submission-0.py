class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        start = 0
        end = len(s)-1

        while start <= end:    
            if s[start] == s[end]:
                start = start + 1
                end = end - 1
            else: 
                return False
        return True
            










#understand
#input: str
#output: bool
    #True if palindrome, False if not
#edge cases: empty string, if theres other characters aside from alphanumeric

#plan
#create the function
    #replace " ", ""
    #start = str[0]
    #end = str[len(str)]
    #while end is not less than start:
        #loop through char:
            #if start == end:
                #increment start
                #decrement end
            #else:
                #return False
    #return true







