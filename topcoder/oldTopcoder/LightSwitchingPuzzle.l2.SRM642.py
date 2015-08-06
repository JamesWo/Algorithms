#http://community.topcoder.com/stat?c=problem_statement&pm=13555
"""
 Problem Statement for LightSwitchingPuzzle
        
Leo has N lights in a row. The lights are numbered 1 through N. Each light is either on or off.

Leo wants to turn all the lights off. He has N switches he may use. The switches are also numbered 1 through N. For each i, switch number i toggles the state of all lights whose numbers are multiples of i. (For example, switch 3 will toggle the state of light 3, light 6, light 9, and so on.)

You are given the current state of all lights as a String state with N characters. For each valid i, state[i] is either 'Y' (meaning that light i+1 is currently on) or 'N' (meaning that the light is off). Determine the smallest number of switches Leo needs to press in order to turn off all the lights. If there is no way to turn off all the lights, return -1 instead.

 
Definition
        
Class:  LightSwitchingPuzzle
Method: minFlips
Parameters:     String
Returns:        int
Method signature:       int minFlips(String state)
(be sure your method is public)
    
 
Constraints
-       state will contain between 1 and 1000 characters, inclusive.
-       Each character of state will be either 'Y' or 'N'.
 
Examples
0)      
        
"YYYYYY"
Returns: 1
We can turn off all the lights by pressing switch 1.
1)      
        
"YNYNYNYNY"
Returns: 2
We cannot turn these lights off in a single step. It can be done in two steps. One possible solution looks as follows: First, press the second switch. This will toggle lights with numbers 2, 4, 6, and 8. The state of the lights after this change will be "YYYYYYYYY". Next, press the first switch to toggle all lightbulbs.

2)      
        
"NNNNNNNNNN"
Returns: 0
All the lights are already off.
3)      
        
"YYYNYYYNYYYNYYNYYYYN"
Returns: 4
4)      
        
"NYNNYNNNYNNNNYNNNNNYNNNNNNYNNNNNNNY"
Returns: 12
"""


"""
analysis:
    every switch is used at most once in the optimal solution.
    we can start at the first switch and decide whether or not to flip it,
    going from left to right.  At each switch, if the light is on, we must flip that switch.
    Each time we flip a switch, update all the switches to the right.
    runtime: O(n^2).
"""
class LightSwitchingPuzzle(object):
    def minFlips(self, state):
        # use a dummy for state[0]
        state = list("x" + state)
        count = 0
        for index in range(1, len(state)):
            if state[index] == "N":
                continue
            elif state[index] == "Y":
                # flip switch
                count += 1
                light = index
                while light < len(state):
                    state[light] = "Y" if state[light] == "N" else "N"
                    light += index
        return count


tester = LightSwitchingPuzzle()

cases = {
"YYYYYY":1,
"YNYNYNYNY":2,
"NNNNNNNNNN":0,
"YYYNYYYNYYYNYYNYYYYN":4,
"NYNNYNNNYNNNNYNNNNNYNNNNNNYNNNNNNNY":12,
}

for inp, expected in cases.iteritems():
    result = tester.minFlips(inp)
    if result != expected:
        print "inp ", inp
        print "result ", result
        print "expected ", expected
        assert False

