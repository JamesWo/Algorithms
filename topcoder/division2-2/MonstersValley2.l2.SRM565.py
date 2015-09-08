"""
# [MonstersValley2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15187&pm=12351)
*Single Round Match 565 Round 1 - Division II, Level Two*

## Statement
Manao is traversing a valley inhabited by monsters. During his journey, he will encounter several monsters one by one. The scariness of each monster is a positive integer. Some monsters may be scarier than others. The i-th (0-based index) monster Manao will meet has scariness equal to dread[i].

Manao is not going to fight the monsters. Instead, he will bribe some of them and make them join him. To bribe the i-th monster, Manao needs price[i] gold coins. The monsters are not too greedy, therefore each value in *price* will be either 1 or 2.

At the beginning, Manao travels alone. Each time he meets a monster, he first has the option to bribe it, and then the monster may decide to attack him. A monster will attack Manao if and only if he did not bribe it and its scariness is strictly greater than the total scariness of all monsters in Manao's party. In other words, whenever Manao encounters a monster that would attack him, he has to bribe it. If he encounters a monster that would not attack him, he may either bribe it, or simply walk past the monster.

![image](images/pic.png)

Consider this example: Manao is traversing the valley inhabited by the Dragon, the Hydra and the Killer Rabbit. When he encounters the Dragon, he has no choice but to bribe him, spending 1 gold coin (in each test case, Manao has to bribe the first monster he meets, because when he travels alone, the total scariness of monsters in his party is zero). When they come by the Hydra, Manao can either pass or bribe her. In the end, he needs to get past the Killer Rabbit. If Manao bribed the Hydra, the total scariness of his party exceeds the Rabbit's, so they will pass. Otherwise, the Rabbit has to be bribed for two gold coins. Therefore, the optimal choice is to bribe the Hydra and then to walk past the Killer Rabbit. The total cost of getting through the valley this way is 2 gold coins.

You are given the int[]s *dread* and *price*. Compute the minimum price Manao will pay to safely pass the valley.

## Definitions
- *Class*: `MonstersValley2`
- *Method*: `minimumPrice`
- *Parameters*: `int[], int[]`
- *Returns*: `int`
- *Method signature*: `int minimumPrice(int[] dread, int[] price)`

## Constraints
- *dread* will contain between 1 and 20 elements, inclusive.
- Each element of *dread* will be between 1 and 2,000,000,000, inclusive.
- *price* will contain between the same number of elements as *dread*.
- Each element of *price* will be either 1 or 2.

## Examples
### Example 1
#### Input
<c>[8, 5, 10],<br />[1, 1, 2]</c>
#### Output
<c>2</c>
#### Reason
The example from the problem statement.

### Example 2
#### Input
<c>[1, 2, 4, 1000000000],<br />[1, 1, 1, 2]</c>
#### Output
<c>5</c>
#### Reason
Manao has to bribe all monsters in the valley.

### Example 3
#### Input
<c>[200, 107, 105, 206, 307, 400],<br />[1, 2, 1, 1, 1, 2]</c>
#### Output
<c>2</c>
#### Reason
Manao can bribe monsters 0 and 3.

### Example 4
#### Input
<c>[5216, 12512, 613, 1256, 66, 17202, 30000, 23512, 2125, 33333],<br />[2, 2, 1, 1, 1, 1, 2, 1, 2, 1]</c>
#### Output
<c>5</c>
#### Reason
Bribing monsters 0, 1 and 5 is sufficient to pass safely.


"""
def find(i, p, seen, dread, price):
    if (i,p) in seen:
        return seen[(i,p)]
    if i < 0 or p < 0:
        seen[(i,p)] = -1
        return -1
    if i == 0:
        res = dread[0] if p >= price[0] else -1
        seen[(i,p)] = res
        return res
    if p == 0:
        seen[(i,p)] = 0
        return 0
    bribe = find(i-1, p-price[i], seen, dread, price)
    noBribe = find(i-1, p, seen, dread, price)
    if noBribe < dread[i]:
        # you must buy
        if p < price[i] or bribe <= 0 or bribe == -1:
            seen[(i,p)] = -1
            return -1
        else:
            seen[(i,p)] = bribe + dread[i]
            return bribe + dread[i]
    else:
        if noBribe == -1:
            seen[(i,p)] = -1
            return -1
        elif bribe == -1:
            seen[(i,p)] = noBribe
            return noBribe
        else:
            result = max(bribe+dread[i], noBribe)
            seen[(i,p)]=result
            return result

def minimumPriceLinear(dread, price):
    for p in range(1, len(dread)*2+1):
        if find(len(dread)-1, p, {}, dread, price) != -1:
            return p
    assert False

def minimumPrice(dread, price):
    lo = 1
    hi = len(dread)*2+1
    while lo < hi:
        mid = ( lo + hi ) / 2
        if find(len(dread)-1, mid, {}, dread, price) == -1:
            lo = mid + 1
        else:
            hi = mid
    return lo





