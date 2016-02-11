#https://www.hackerrank.com/challenges/jim-and-the-orders

numOrders = input()
orders = []
for i in range(numOrders):
    orders.append((i+1, sum(map(int, raw_input().split(" ")))))
orders.sort(key=lambda x:x[1])
print " ".join(map(lambda x:str(x[0]), orders))

