"""
A classic example of an optimization problem involves making change using the fewest coins. 

Let’s start with identifying the base case. If we are trying to make change for the same amount as the value of one of our coins, the answer is easy, one coin.

If the amount does not match we have several options. What we want is the minimum of a penny plus the number of coins needed to make change for the original amount minus a penny, or a nickel plus the number of coins needed to make change for the original amount minus five cents, or a dime plus the number of coins needed to make change for the original amount minus ten cents, and so on. 

"""

# inefficient
def recMC(coinValueList, change):
    minCoins = change
    # base
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c < change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

# print(recMC([1,5,10,25], 63))

# A simple solution is to store the results for the minimum number of coins in a table when we find them. 
def recMC(coinValueList, change, knownResults):
    minCoins = change
    # base
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    # we have added a test to see if our table contains the minimum number of coins for a certain amount of change.
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c < change]:
            numCoins = 1 + recMC(coinValueList, change-i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
                print(knownResults)
    return minCoins

print(recMC([1,5,10,25], 63, [0]*64))

# Our dynamic programming solution is going to start with making change for one cent and systematically work its way up to the amount of change we require. 

# Below is a dynamic programming algorithm to solve our change-making problem. dpMakeChange takes three parameters: a list of valid coin values, the amount of change we want to make, and a list of the minimum number of coins needed to make each value. When the function is done minCoins will contain the solution for all values from 0 to the value of change.

def dpMakeChange(coinValueList, change, minCoins):
    # get the solution for all values from 0 to the value of change.
    for cents in range(change+1):
        coinCount = cents  # max
        # get the min coinCount for each cents
        for i in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-i] + 1 < coinCount:
                coinCount = minCoins[cents-i] + 1
        minCoins[cents] = coinCount
        print(minCoins)
    return minCoins[change]

print(recMC([1,5,10,25], 63, [0]*64))







