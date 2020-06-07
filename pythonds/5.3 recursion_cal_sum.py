"""
recursion:
Calculating the Sum of a List of Numbers using recursion
𝑙𝑖𝑠𝑡𝑆𝑢𝑚(𝑛𝑢𝑚𝐿𝑖𝑠𝑡)=𝑓𝑖𝑟𝑠𝑡(𝑛𝑢𝑚𝐿𝑖𝑠𝑡)+𝑙𝑖𝑠𝑡𝑆𝑢𝑚(𝑟𝑒𝑠𝑡(𝑛𝑢𝑚𝐿𝑖𝑠𝑡))

"""
def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])

print(listsum([1,2,3,5,7]))
