import random
from collections import Counter

def build_weighted_pool(draws):
    all_nums = [num for draw in draws for num in draw]
    freq = Counter(all_nums)
    pool = []
    for num, count in freq.items():
        pool.extend([num] * count)
    return pool, freq

def simulate_draws(draws, picks=6, simulations=100000):
    pool, freq = build_weighted_pool(draws)
    results = Counter()
    for _ in range(simulations):
        combo = tuple(sorted(random.sample(pool, picks)))
        results[combo] += 1
    return results.most_common(6), freq
