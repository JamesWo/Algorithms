"""
https://community.topcoder.com/stat?c=problem_statement&pm=14074
Recently you learned about substitution ciphers. This problem is about such a cipher. All strings in this problem (both encrypted and decrypted ones) will consist of only uppercase English letters ('A'-'Z').

When encrypting text using a substitution cipher we choose a substitution table: a permutation p of the alphabet. In other words, for each letter x in the alphabet we choose a letter p(x) that will be used to encode x. This encoding must be one-to-one: if x and y are two different letters, the letters p(x) and p(y) chosen to encode them must also be different.

You decided to try it out: you chose some specific substitution table and used it to encrypt some strings.

At some later point in time you found an encrypted string y. You believe it was encrypted using the substitution table you once had. Sadly, you do not remember the substitution table anymore. The only thing you remember about it is that when you used it to encrypt the string a you got the string b. Is this information sufficient to decrypt y?

You are given the Strings a, b, and y. If it is possible to decrypt the string y, return the original string x that was encrypted into y. (More precisely: If there is exactly one string x such that the same permutation table can be used to encrypt a into b and to encrypt x into y, return x.) Otherwise, return an empty string.

Definition
        
Class:  SubstitutionCipher
Method: decode
Parameters: String, String, String
Returns:    String
Method signature:   String decode(String a, String b, String y)
(be sure your method is public)
    
 
Constraints
-   a will contain between 1 and 50 characters, inclusive.
-   a and b will contain the same number of characters.
-   It is guaranteed that b can be obtained from a by applying some substitution cipher.
-   y will contain between 1 and 50 characters, inclusive.
-   Each character in a, b, and y will be an uppercase English letter ('A'-'Z').
 
"""

import string

class SubstitutionCipher:
    def decode(self, a, b, y):
        invMap = {}
        for i in range(len(a)):
            invMap[b[i]] = a[i]
        if len(invMap) == len(string.ascii_uppercase)-1:
            #if we've seen 25 character mappings, we know the full permutation
            missingKey = (set(string.ascii_uppercase) - set(invMap.keys())).pop()
            missingVal = (set(string.ascii_uppercase) - set(invMap.values())).pop()
            invMap[missingKey] = missingVal
        result = []
        for char in y:
            if char not in invMap:
                return ""
            result.append(invMap[char])
        return "".join(result)



cases = [
    [("CAT", "DOG", "GOD"), "TAC"],
    [("BANANA", "METETE", "TEMP"), ""],
    [("THEQUICKBROWNFOXJUMPSOVERTHELAZYHOG", "UIFRVJDLCSPXOGPYKVNQTPWFSUIFMBAZIPH", 
        "DIDYOUNOTICESKIPPEDLETTER"), "CHCXNTMNSHBDRJHOODCKDSSDQ"]
]
solution = SubstitutionCipher()
for inp, expectedOutput in cases:
    result = solution.decode(*inp)
    if result != expectedOutput:
        print "test failed"
        print "input: ", inp
        print "result: ", result
        print "expected: ", expectedOutput
        assert False
        
