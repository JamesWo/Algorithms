# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB=input()
BC=input()
hyp = float( math.sqrt( ( AB**2 + BC**2 ) ) )
MC = hyp/float(2)

angleC = float( ( math.asin( AB/hyp ) ) )
MB = math.sqrt( BC**2 + MC**2 -2*BC*MC*math.cos(angleC) )

theta = math.degrees( math.acos(float(MC**2-MB**2-BC**2)/float(-2*MB*BC)) )
print str(int(round(theta))) + "°"

