import itertools
K, M = map( int, raw_input().split( " " ) )
print max((sum(map(lambda x: x*x, nums))%M) for nums in itertools.product(*[map(int, raw_input().split(" "))[1:] for _ in range(K) ]))
