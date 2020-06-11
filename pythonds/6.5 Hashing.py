"""

Hashing - O(1)
with collision - depends on load factor

# Our goal is to create a hash function that minimizes the number of collisions, is easy to compute, and evenly distributes the items in the hash table.

- The folding method for constructing hash functions begins by dividing the item into equal-size pieces (the last piece may not be of equal size). For example, if our item was the phone number 436-555-4601, we would take the digits and divide them into groups of 2 (43,65,55,46,01). After the addition, 43+65+55+46+01, we get 210. If we assume our hash table has 11 slots, then we need to perform the extra step of dividing by 11 and keeping the remainder. In this case 210 % 11 is 1.

- Another numerical technique for constructing a hash function is called the mid-square method. We first square the item, and then extract some portion of the resulting digits. For example, if the item were 44, we would first compute 442=1,936. By extracting the middle two digits, 93, and performing the remainder step, we get 5 (93 % 11).

"""

# hash a string
def hash(astring, tablesize):
    sums = 0
    for i in range(len(astring)):
        sums = sums + ord(astring[i])  # ord['a'] = 97

    return sums % tablesize

# collision resolution
# linear probing
# find the next slot that is available
# it is essential that we utilize the same methods to search for items. What if we are looking for 20? Now the hash value is 9, and slot 9 is currently holding 31. We cannot simply return False since we know that there could have been collisions. We are now forced to do a sequential search, starting at position 10, looking until either we find the item 20 or we find an empty slot.

# A disadvantage to linear probing is the tendency for clustering; items become clustered in the table. This means that if many collisions occur at the same hash value, a number of surrounding slots will be filled by the linear probing resolution. - reharshing

# quadratic probing
# we use a rehash function that increments the hash value by 1, 3, 5, 7, 9, and so on. 

# Chaining
# When collisions happen, the item is still placed in the proper slot of the hash table using linked list.






