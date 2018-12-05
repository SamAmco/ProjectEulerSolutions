coin_values = [200,100,50,20,10,5,2,1]

class Solution:
    def __init__(self, coins):
        self.coins = sorted(coins)

    def __repr__(self):
        return ','.join(str(x) for x in self.coins)

    def __eq__(self, other):
        return self.coins == other.coins

    def __hash__(self):
        return hash(self.__repr__())


class SolutionCounter:
    def __init__(self):
        self.solutions = set()

    def add_solution(self, solution):
        self.solutions.add(Solution(solution))


def count_ways_to_make_X_recursive(current_count, previous_coins, solution_counter, X):
    #print("Received: \n%s \n%s \n%s \n%s" % (current_count, previous_coins, solution_counter, X))
    if current_count > X:
        return
    elif current_count == X:
        solution_counter.add_solution(previous_coins)

    allowed_coins = coin_values
    if(current_count > 0):
        allowed_coins = coin_values[coin_values.index(previous_coins[-1]):]

    for v in allowed_coins:
        count_ways_to_make_X_recursive(current_count + v, list(previous_coins) + [v], solution_counter, X)

solution_counter = SolutionCounter()
count_ways_to_make_X_recursive(0, [], solution_counter, 200)
print(len(solution_counter.solutions))
