from hashtable import hashTable

def main():

    myHash = hashTable(17)

    myHash.add(10, "This is 10")

    print(myHash.exist(10))
    print(myHash.get(10))

    myHash.remove(10)

    # remove again
    myHash.remove(10)

if __name__ == '__main__':
    main()
