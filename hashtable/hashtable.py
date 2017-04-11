class hashTable(object):
    """
    Simple implementation of hash table with
    linear probing.
    Methods: hash, add, exists, get, remove
    """

    def __init__(self, size):
        self.size = size
        self.table = [None]*size

    def add(self, key, value):
        # generate key-value pairs and hash with linear probing
        key_value_pair = [key, value]
        key_hash = key % self.size
        i = 0
        while self.table[key_hash] and i <= self.size:
            if key_hash == self.size - 1:
                key_hash = 0
            else:
                key_hash += 1
            i += 1
        if i > self.size:
            print("the hash table is full")
        else:
            self.table[key_hash] = key_value_pair

    def exist(self, key):
        key_hash = key % self.size
        i = 0
        while i <= self.size:
            if key == self.table[key_hash][0]:
                return True
            i += 1
        return False

    def get(self, key):
        key_hash = key % self.size
        i = 0
        while i <= self.size:
            if key == self.table[key_hash][0]:
                return self.table[key_hash][1]
            i += 1
        print("value not in table")

    def remove(self, key):
        key_hash = key % self.size
        i = 0
        while i <= self.size:
            if key == self.table[key_hash][0]:
                self.table[key_hash] = "Deleted"
                print("key deleted")
                return
            i += 1
        print("key does not exist")











