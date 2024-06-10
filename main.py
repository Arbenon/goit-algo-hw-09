import timeit
import random

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            amount -= num_coins * coin
            result[coin] = num_coins
    
    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)
    
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result

def measure_performance():
    small_amounts = [random.randint(1, 100) for _ in range(10)]
    large_amounts = [random.randint(1000, 10000) for _ in range(10)]
    
    # Вимірювання жадібного алгоритму для маленької кількості
    greedy_small_time = timeit.timeit(
        stmt='find_coins_greedy(amount)', 
        setup='from __main__ import find_coins_greedy; amount=random.choice(small_amounts)',
        globals={'find_coins_greedy': find_coins_greedy, 'random': random, 'small_amounts': small_amounts},
        number=1000
    )
    
    # Вимірювання ДП алгоритму для маленької кількості
    dp_small_time = timeit.timeit(
        stmt='find_min_coins(amount)', 
        setup='from __main__ import find_min_coins; amount=random.choice(small_amounts)',
        globals={'find_min_coins': find_min_coins, 'random': random, 'small_amounts': small_amounts},
        number=1000
    )
    
    # Вимірювання жадібного алгоритму для великої кількості
    greedy_large_time = timeit.timeit(
        stmt='find_coins_greedy(amount)', 
        setup='from __main__ import find_coins_greedy; amount=random.choice(large_amounts)',
        globals={'find_coins_greedy': find_coins_greedy, 'random': random, 'large_amounts': large_amounts},
        number=1000
    )
    
    # Вимірювання ДП алгоритму для великої кількості
    dp_large_time = timeit.timeit(
        stmt='find_min_coins(amount)', 
        setup='from __main__ import find_min_coins; amount=random.choice(large_amounts)',
        globals={'find_min_coins': find_min_coins, 'random': random, 'large_amounts': large_amounts},
        number=1000
    )
    
    return {
        "greedy_small_time": greedy_small_time,
        "dp_small_time": dp_small_time,
        "greedy_large_time": greedy_large_time,
        "dp_large_time": dp_large_time
    }

# Презентація вимірів
performance = measure_performance()
print(f'\nВимір жадібного алгоритму на маленькій кількості монет:       {performance["greedy_small_time"]}')
print(f'Вимір дп алгоритму на маленькій кількості монет:              {performance["dp_small_time"]}')
print(f'Вимір жадібного алгоритму на великій кількості монет:         {performance["greedy_large_time"]}')
print(f'Вимір дп алгоритму на великій кількості монет:                {performance["dp_large_time"]}\n')
