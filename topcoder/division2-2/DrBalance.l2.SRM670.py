"""
https://community.topcoder.com/stat?c=problem_statement&pm=14060

Problem Statement
        
A plus/minus string is a string in which each character is either a '+' or a '-'.

The balance of a plus/minus string is computed as the number of '+' characters minus the number of '-' characters.
For example, the balance of the string "++-+" is 3-1 = 2, and the balance of the string "---" is 0-3 = -3.

The prefix of a string S is any string that can be obtained by removing some (possibly none, possibly all) characters from the end of S. For example, the prefixes of the string "++-+" are the strings "++-+", "++-", "++", "+", and "".

Given a plus/minus string, its negativity is the number of its prefixes that have a negative balance. For example, the negativity of the string "++-+" is 0, as none of its prefixes have a negative balance. The negativity of the string "---" is 3. Its three prefixes with a negative balance are "-", "--", and "---".

You are given a String s that is a plus/minus string. You are also given an int k. Your goal is to change s into a string with negativity at most k. In other words, you want to change s into a string that has at most k prefixes that have a negative balance.

In order to change s you are going to perform a sequence of zero or more steps. In each step you can change a single '-' character in s into a '+' or vice versa. Compute and return the smallest number of steps needed.

 
Definition
        
Class:  Drbalance
Method: lesscng
Parameters: String, int
Returns:    int
Method signature:   int lesscng(String s, int k)
(be sure your method is public)
    
 
Constraints
-   s will contain between 1 and 50 characters, inclusive.
-   k will be between 0 and the length of s, inclusive.
-   Each character in s will be either '+' or '-'.
 
"""

class Drbalance:
    def lesscng(self, string, maxNegativity):
        stringArray = list(string)
        changedCount = 0
        for i in range(len(string)):
            if self.negativity(stringArray) <= maxNegativity:
                return changedCount
            if stringArray[i] == '-':
                stringArray[i] = '+'
                changedCount += 1
        return changedCount

    def negativity(self, stringArray):
        negativeCount = 0
        balance = 0
        for char in stringArray:
            if char == '-':
                balance -= 1
            elif char == "+":
                balance += 1
            else:
                assert False, "incorrect character in string: %c" % char
            if balance < 0:
                negativeCount += 1
        return negativeCount




cases = [
    [["---", 1], 1],
    [["+-+-", 0], 0],
    [["-+-+---", 2],1],
    [["-------++", 3],3],
    [["-+--+--+--++++----+", 3],2]
]

solution = Drbalance()
for inp, expectedOutput in cases:
    result = solution.lesscng(*inp)
    if result != expectedOutput:
        print "test failed"
        print "input: ", inp
        print "result: ", result
        print "expected: ", expectedOutput
        assert False
 
