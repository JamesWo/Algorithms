"""
# [SurveillanceSystem](http://community.topcoder.com/tc?module=ProblemDetail&rd=15501&pm=12588)
*Single Round Match 581 Round 1 - Division I, Level One*

## Statement
There is a long narrow storehouse.
The storehouse is divided into a sequence of N identical sectors, labeled 0 through N-1.
Each sector is large enough to contain a single container.
Currently, some sectors are empty and some sectors are filled by containers.
The storehouse also contains a surveillance system that is described below.

We are going to break into the storehouse.
As a part of preparation for the heist, we already found out some information about the warehouse.
In particular, we know exactly how the containers are currently placed in the warehouse.
You are given a String *containers* consisting of N characters.
For each i, character i of *containers* is 'X' if sector i contains a container, and it is '-' if sector i is empty.

We also discovered some information about the surveillance system.
The system consists of several hidden cameras.
You are given a int *L* with the following meaning:
Each of the cameras monitors exactly *L* consecutive sectors.
The segments of sectors monitored by different cameras might overlap, but no two cameras watch exactly the same segment.
(In other words, each sector may be monitored by multiple cameras, but each camera monitors a different set of consecutive sectors.)

Finally, we know something about what the cameras currently see.
You are given a int[] *reports*.
Each element of *reports* corresponds to one of the cameras (in no particular order).
More precisely, *reports*[i] is the number of containers stored in the sectors monitored by the corresponding camera.

It is guaranteed that all our information is correct and consistent.

Your task is to use the provided information to deduce which sectors are monitored by at least one surveillance camera.
Return a String containing N characters.
For each i, character i of the return value should be one of '+', '?', and '-'.
Character '+' represents that sector i is certainly monitored by at least one camera.
Character '-' represents that sector i is certainly not monitored by any of the cameras.
Character '?' represents the remaining case: given the information we have, it is possible that sector i is monitored, but it is also possible that it is not monitored.

## Definitions
- *Class*: `SurveillanceSystem`
- *Method*: `getContainerInfo`
- *Parameters*: `String, int[], int`
- *Returns*: `String`
- *Method signature*: `String getContainerInfo(String containers, int[] reports, int L)`

## Constraints
- *containers* will contain N elements, where N is between 1 and 50, inclusive.
- Each character in *containers* will be either 'X' or '-'.
- *L* will be between 1 and N, inclusive.
- *reports* will contain between 1 and N-*L*+1 elements, inclusive.
- Each element of *reports* will be between 0 and *L*, inclusive.
- The given information will be consistent.

## Examples
### Example 1
#### Input
<c>"-X--XX",<br />[1, 2],<br />3</c>
#### Output
<c>"??++++"</c>
#### Reason
This storehouse has 6 sectors.
There are containers in sectors 1, 4, and 5.
There are two cameras: camera #0 monitors 1 container, and camera #1 monitors 2 containers.
Clearly, camera #1 must be watching sectors 3, 4, and 5.
Camera #0 may be watching sectors (0, 1, 2), (1, 2, 3), or (2, 3, 4).
Thus, camera #0 is surely monitoring sector 2.
Sectors 0 and 1 may or may not be monitored.

### Example 2
#### Input
<c>"-XXXXX-",<br />[2],<br />3</c>
#### Output
<c>"???-???"</c>
#### Reason
The camera is monitoring either the leftmost or the rightmost segment, thus the middle sector is surely not under surveillance.

### Example 3
#### Input
<c>"------X-XX-",<br />[3, 0, 2, 0],<br />5</c>
#### Output
<c>"++++++++++?"</c>
#### Reason
We can deduce that cameras #1 and #3 are watching segments (0, 1, 2, 3, 4) and (1, 2, 3, 4, 5). Camera #2 is monitoring the segment (4, 5, 6, 7, 8), since this is the only segment with two occupied sectors. Camera #0 is either watching (5, 6, 7, 8, 9) or (6, 7, 8, 9, 10), thus the rightmost sector might have slipped from the surveillance.

### Example 4
#### Input
<c>"-XXXXX---X--",<br />[2, 1, 0, 1],<br />3</c>
#### Output
<c>"???-??++++??"</c>
### Example 5
#### Input
<c>"-XX--X-XX-X-X--X---XX-X---XXXX-----X",<br />[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],<br />7</c>
#### Output
<c>"???++++?++++++++++++++++++++??????--"</c>

"""
def fill( result, report, count, segments, L ):
    arr = [ 0 ] * len( result )
    for s in segments:
        for index in range( s, s+L ):
            arr[index] += 1
    for index in range( len( arr ) ):
        if arr[index] == 0:
            continue
        if arr[index] < ( len(segments) + 1 - count ):
            if result[index] != "+":
                #print "setting %d to ?" % index, result
                result[index] = '?'
        else:
            result[index] = '+'

def getContainerInfo(containers, reports, L):
    result = [ "-" ] * len( containers )
    reports.sort()
    # maps number of camers to starting index of segments of size L
    segments = {}
    for i in range( len( containers )+1 ):
        segments[ i ] = []
    for start in range(0, len( containers ) - L + 1 ):
        numX = 0
        for index in range( start, start+L ):
            if containers[index] == "X":
                numX += 1
        segments[ numX ].append( start ) 
    for report in sorted( list( set( reports ) ) ):
        count = reports.count( report )
        if count < len( segments[report] ):
            fill( result, report, count, segments[report], L )
        elif count == len( segments[report] ):
            for s in segments[ report ]:
                for index in range( s, s+L ):
                    result[index] = "+"
            # mark as +
        else:
            assert False, " %s  %s " % ( str( count ), str( segments[report] ) )
    return "".join( result )

















































