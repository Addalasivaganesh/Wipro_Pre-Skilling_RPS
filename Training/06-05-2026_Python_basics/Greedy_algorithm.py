
def min_coins(amount):
    coins = [10, 5, 2, 1]
    count = 0

    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count
print(min_coins(15))