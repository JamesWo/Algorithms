#http://community.topcoder.com/stat?c=problem_statement&pm=13678


"""

Problem Statement for ValueOfString


Problem Statement
        
You are given a String s consisting of lower case letters. We assign the letters 'a' to 'z' values of 1 to 26, respectively. We will denote the value assigned to the letter X by val[X]. For example, val['a'] = 1 and val['e'] = 5.

We define the value of the string s as follows. For each letter s[i], let k[i] be the number of letters in s that are less than or equal to s[i], including s[i] itself. Then, the value of s is defined to be the sum of k[i] * val[s[i]] for all valid i.

Given the string, compute and return the value of the string.

 
Definition
        
Class:  ValueOfString
Method: findValue
Parameters:     String
Returns:        int
Method signature:       int findValue(String s)
(be sure your method is public)
    
 
Constraints
-       s will contain between 1 and 50 characters, inclusive.
-       s will consist of lowercase letters ('a'-'z').
 
"""

class ValueOfString(object):
    def findValue(self, s):
        value = 0
        letters = [0]*27 # since we are 1-indexed
        for char in s:
            charVal = ord(char) - ord('a') + 1
            letters[charVal] += 1
        for char in s:
            charVal = ord(char) - ord('a') + 1
            numSmaller = sum(letters[0:charVal+1])
            value += numSmaller*charVal
        return value


# test

cases = {

"babca": 35,
        
"zz": 104,
        
"y": 25,
        
"aaabbc": 47,
        
"topcoder": 558,
        
"thequickbrownfoxjumpsoverthelazydog": 11187,
        
"zyxwvutsrqponmlkjihgfedcba": 6201,

}


tester = ValueOfString()

for inp, expected in cases.iteritems():
    result = tester.findValue(inp)
    if result != expected:
        print "inp ", inp
        print "result ", result
        print "expected ", expected
        assert False














