from queue import queue

def main():

    myQueue = queue()

    element = [2,1,2,3,1]

    # enqueue
    for i in element:
        myQueue.enqueue(i)
        print(myQueue)

    # dequeue
    for i in element:
        myQueue.dequeue()
        print(myQueue)


if __name__ == "__main__":
    main()