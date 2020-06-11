"""
Hashtable with collision
Map() Create a new, empty map. It returns an empty map collection.

put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.

get(key) Given a key, return the value stored in the map or None otherwise.

del Delete the key-value pair from the map using a statement of the form del map[key].

len() Return the number of key-value pairs stored in the map.

in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.

"""
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    # The put function (see Listing 3) assumes that there will eventually be an empty slot unless the key is already present in the self.slots. It computes the original hash value and if that slot is not empty, iterates the rehash function until an empty slot occurs. If a nonempty slot already contains the key, the old data value is replaced with the new data value. 
    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        # check if it is an empty slot
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        # if the key already exists at that spot
        elif self.slots[hashvalue] == key: # replace
            self.data[hashvalue] = data
        # the spot stores another key
        # find the next empty slot or find the key
        else: 
            nextslot = self.rehash(hashvalue, len(self.slots))
            # find the empty nextslot or find the nextslot that store the key
            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot, len(self.slots))
            # find the next empty slot
            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data
            else: # self.data[nextslot] == key, replace data
                self.data[nextslot] = data 

    def hashfunction(self, key, size):
        return key % size

    # The collision resolution technique is linear probing with a “plus 1” rehash function. 
    def rehash(self, oldvalue, size):
        return (oldvalue + 1) % size

    #  the get function begins by computing the initial hash value. If the value is not in the initial slot, rehash is used to locate the next possible position. 
    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        found, stop = False, False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot: # return back to the inital slot
                    stop = True

        if found:
            return self.data[position]
        else:
            return None
        """
        hashvalue = self.hashfunction(key, len(self.slots))
        stop = False
        if self.slots[hashvalue] == key:
            return self.data[hashvalue]
        elif self.slots[hashvalue] == None:
            return None
        else: # find the next slot that might store the key
            nextslot = self.rehash(hashvalue, len(self.slots))
            while self.slots[nextslot] != key and not stop:
                nextslot = self.rehash(nextslot, len(self.slots))
                if nextslot == hashvalue:
                    stop = True

            if self.slots[nextslot] == key:
                return self.data[nextslot]
            else:
                return None
        """
    # overload the __getitem__ and __setitem__ methods to allow access using``[]``. This means that once a HashTable has been created, the familiar index operator will be available.
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

if __name__ == '__main__':
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)
    print(H[20])
    print(H[17])
    H[20] = "duck"
    print(H[20])
    print(H.data)
    print(H[99])
