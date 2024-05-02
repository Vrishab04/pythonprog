from collections import OrderedDict
order = OrderedDict()
n = int(input())
for _ in range(n):
    item, _, price = input().rpartition(' ')
    order[item] = order.get(item, 0) + int(price)
for item, price in order.items():
    print(item, price)