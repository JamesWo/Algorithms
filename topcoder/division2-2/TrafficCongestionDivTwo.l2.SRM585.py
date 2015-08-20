def theMinCars(treeHeight):
     counts = [ 0 ] * (treeHeight+2)
     counts[ 0 ] = 1
     counts[ 1 ] = 1
     for i in range(2, treeHeight+1):
         counts[ i ] = 1
         for j in range( 0, i-1 ):
             counts[ i ] += 2 * counts[ j ]
     return counts[ treeHeight ]

