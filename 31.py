coin_values = [200,100,50,20,10,5,2,1]

def count_ways_to_make_X(current_count, X, last_coin = coin_values[0]):
    if current_count > X:
        return 0
    elif current_count == X:
        return 1

    allowed_coins = coin_values[coin_values.index(last_coin):]

    return sum(map(lambda v : count_ways_to_make_X(current_count + v, X, v), allowed_coins))

print(count_ways_to_make_X(0, 200))
