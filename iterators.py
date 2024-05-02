from itertools import combinations

def calculate_probability(N, K, letters):
    N_a = letters.count('a')
    if N_a == 0:
        return 0.0
    elif N - N_a < K:
        return 1.0
    else:
        num = len(list(combinations(range(1, N + 1), K)))
        total = len(list(combinations(range(1, N + 1), K)))
        return (total - num) / total

N = int(input())
letters = input().split()
K = int(input())
print("{:.4f}".format(calculate_probability(N, K, letters)))