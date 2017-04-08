# a self build class for array

def myArray():

    myarr = [1,2,3,4,5]

    # get size
    print(len(myarr))

    # is_empty
    print(len(myarr) == 0)

    # push at end
    myarr.append(6)

    # insert
    myarr.insert(1,1.5)
    print(myarr)

    # prepend
    myarr.insert(0,0)
    print(myarr)

    # pop
    myarr.pop()
    print(myarr)

    # delete (the first equal value)
    myarr.remove(0)
    print(myarr)

    # find
    try:
        print(myarr.index(1))
    except ValueError:
        print(-1)

    try:
        myarr.index(10)
    except ValueError:
        print(-1)

    # reverse
    myarr.reverse()
    print(myarr)

    # sort
    myarr.sort()
    print(myarr)


def main():
    myArray()

if __name__ == '__main__':
    main()
