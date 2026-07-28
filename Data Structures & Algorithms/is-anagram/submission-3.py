class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    #understand
    #input: 2 strings
    #output: true if they both strings for the same characters, false if not
    #edgecase: empty, only one element, different cases(uppercase or lowercase), different lenghts

    #plan

    #if not s or not t:
        #return false

    #if diff lengths :
        #return false
    
    #s = s.lower()
    #t = t.lower()

    #create dictionary for both s and t
        #if char not in dict:
            #add it
        #else:      
            #increment it
        
        #compre and return true or false
    

        if not s or not t:
            return False
        
        if len(s) != len(t):
            return False

        s = s.lower()
        t = t.lower()

        char_s = {}

        for char in s:
            if char not in char_s:
                char_s[char] = 1
            else:
                char_s[char] += 1

        char_t = {}

        for char in t:
            if char not in char_t:
                char_t[char] = 1
            else:
                char_t[char] += 1
        
        return char_s == char_t