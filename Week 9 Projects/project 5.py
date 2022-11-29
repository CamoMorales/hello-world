def isSorted(myList):
    if len(myList) < 2:
        return True
    for i in range(len(myList) - 1):
        if myList[i] > myList[i+1]:
            return False
        return True

def main():
    liist = []
    print(isSorted(liist))
    liist = [1]
    print(isSorted(liist))
    liist = list(range(10))
    print(isSorted(liist))
    liist[9] = 3
    print(isSorted(liist))

if __name__ == '__main__':
    main()
