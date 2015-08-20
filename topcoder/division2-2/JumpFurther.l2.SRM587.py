"""
# [JumpFurther](http://community.topcoder.com/tc?module=ProblemDetail&rd=15699&pm=12300)
*Single Round Match 587 Round 1 - Division I, Level One*

## Statement
Little Fox Jiro is standing at the bottom of a long flight of stairs.
The bottom of the stairs has number 0, the bottommost step has number 1, the next step has number 2, and so on.
The staircase is so long that Jiro is guaranteed not to reach its top.

Jiro will now perform *N* consecutive actions.
The actions are numbered 1 through *N*, in order.
When performing action X, Jiro chooses between two options: either he does nothing, or he jumps exactly X steps up the stairs.
In other words, if Jiro starts performing action X standing on step Y, he will end it either on step Y, or on step Y+X.

For example, if *N*=3, Jiro will make three consecutive choices: whether or not to jump 1 step upwards, 2 steps upwards, and then 3 steps upwards.

One of the steps is broken.
The number of this step is *badStep*.
Jiro cannot jump onto this step.

You are given the ints *N* and *badStep*.
Compute and return the number of the topmost step that can be reached by Jiro.

## Definitions
- *Class*: `JumpFurther`
- *Method*: `furthest`
- *Parameters*: `int, int`
- *Returns*: `int`
- *Method signature*: `int furthest(int N, int badStep)`

## Constraints
- *N* will be between 1 and 2,000, inclusive.
- *badStep* will be between 1 and 4,000,000, inclusive.

## Examples
### Example 1
#### Input
<c>2,<br />2</c>
#### Output
<c>3</c>
#### Reason
The optimal strategy is to jump upwards twice: from step 0 to step 1, and then from step 1 to step 3. This trajectory avoids the broken step.

### Example 2
#### Input
<c>2,<br />1</c>
#### Output
<c>2</c>
#### Reason
In this case step 1 is broken, so Jiro cannot jump upwards as his first action. The optimal strategy is to first stay on step 0, and then to jump from step 0 to step 2.

### Example 3
#### Input
<c>3,<br />3</c>
#### Output
<c>5</c>
### Example 4
#### Input
<c>1313,<br />5858</c>
#### Output
<c>862641</c>
### Example 5
#### Input
<c>1,<br />757065</c>
#### Output
<c>1</c>

"""
def furthest(N, badStep):
    total = 0
    foundBad = False
    for i in range(1, N+1):
        # take jump i
        total += i
        if total == badStep:
            foundBad = True
    if foundBad:
        return total - 1
    else:
        return total

