"""

# [ChooseTheBestOne](http://community.topcoder.com/tc?module=ProblemDetail&rd=15852&pm=13146)
*Single Round Match 619 Round 1 - Division II, Level Two*

## Statement
Shiny wants to give an award to one of the employees in her company.
However, all her employees are doing perfect work, so it's hard to pick the one that gets the award.
Therefore Shiny organized a game they will play to determine the winner.

At the beginning of the game, all *N* employees form a circle.
Then, they receive t-shirts with numbers 1 through *N* in clockwise order along the circle.
These numbers are never used in the game, we will just use them to identify the winner.

The game is played in turns.
The turns are numbered starting from 1.
In each turn, Shiny starts by standing in front of some employee (as specified below) and saying "one".
Then she moves clockwise along the circle to the next employee and says "two".
And so on, until the number she says reaches the threshold for that particular turn.
The threshold for turn number t is t^3.
(That is, the threshold is 1 for turn 1, 8 for turn 2, 27 for turn 3, and so on.)

At the end of each turn, the employee currently standing in front of Shiny (i.e., the one that received the number t^3) is eliminated.
In the very first round Shiny starts in front of the employee with the number 1 on their t-shirt.
In each of the following rounds, Shiny starts in front of the next employee clockwise from the one who just got eliminated.

When there is only one employee left in the game, the game ends and the employee wins the award.

You are given the int *N*.
Return the t-shirt number of the employee who gets the award.

## Definitions
- *Class*: `ChooseTheBestOne`
- *Method*: `countNumber`
- *Parameters*: `int`
- *Returns*: `int`
- *Method signature*: `int countNumber(int N)`

## Constraints
- *N* will between 1 and 5000, inclusive.

## Examples
### Example 1
#### Input
<c>3</c>
#### Output
<c>2</c>
#### Reason
In the first round, Shiny stands in front of employee 1, says "one" and eliminates him.
In the second round, Shiny starts in front of employee 2. She says "one" to employee 2, "two" to
employee 3, "three" to employee 2 again, ..., and "eight" to employee 3. Thus, employee 3 
gets eliminated and employee 2 wins the award.

### Example 2
#### Input
<c>6</c>
#### Output
<c>6</c>
### Example 3
#### Input
<c>10</c>
#### Output
<c>8</c>
### Example 4
#### Input
<c>1234</c>
#### Output
<c>341</c>
"""


def countNumber(N):
    persons = range(1, N+1)
    t = 1
    index = 0
    while len(persons) > 1:
        step = t**3
        index = index + step - 1
        index = index % len(persons)
        persons = persons[:index] + persons[index+1:]
        t += 1
    return persons[0]

