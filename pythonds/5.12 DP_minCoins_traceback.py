"""

# Although our making change algorithm does a good job of figuring out the minimum number of coins, it does not help us make change since we do not keep track of the coins we use.
# keep track of the coins used, along with a function printCoins that walks backward through the table to print out the value of each coin used. 

"""
# keep track of the coins used, only store the last coin used
def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    # get the solution for all values from 0 to the value of change.
    for cents in range(change+1):
        coinCount = cents  # max
        newCoin = 1        # minimum is 1
        # get the min coinCount for each cents
        for i in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-i] + 1 < coinCount:
                coinCount = minCoins[cents-i] + 1
                newCoin = i  # keep the last coin that gives minimum coin count
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin  
        #print(coinsUsed)
        #print(minCoins)
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        lastcoin = coinsUsed[coin]
        print(lastcoin)
        coin = coin - lastcoin

def main():
    amnt = 45
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1) # store the last coin that gives minimum coin count
    coinCount = [0]*(amnt+1)

    print(f"making changes for {amnt}")
    print(f"the minimum number of coins used is {dpMakeChange(clist, amnt, coinCount, coinsUsed)}")
    print("they are: ")
    printCoins(coinsUsed, amnt)

main()
