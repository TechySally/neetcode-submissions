class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    #understand
    #input: 2 strings
    #output: true if they both strings for the same characters, false if not
    #edgecase: empty, only one element, different cases(uppercase or lowercase), different lenghts

    #plan

    #if not s or if not t:
        #return false
    
    #s = s.lower()
    #t = t.lower()

    #create an empty list (characters)
    #loop through the first string and add every character to the list
    #loop through second list 
        #if a letter isnt in characters:
            #return false
    #return true

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

        if len(char_t) != len(char_s):
            return False

        
        return char_s == char_t