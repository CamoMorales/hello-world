def mean(list):
    if len(list) == 0:
        return 0
    list.sort()
    total = 0
    for number in list:
        total += number
    return total / len(list)

def median(list):
    if len(list) == 0:
        return 0
    list.sort()
    medIndex = len(list) // 2
    if len(list) % 2 == 1:
        return list[medIndex]
    else:
        return(list[medIndex] + list[medIndex - 1]) / 2

def mode(list):
    numDictionary = {}
    for digit in list:
        number = numDictionary.get(digit, None)
        if number == None:

            numDictionary[digit] = 1
        else:
            numDictionary[digit] = number + 1
            maxValue = max(numDictionary.values())
        moList = []
        for key in numDictionary:
            if numDictionary[key] == maxValue:
                moList.append(key)
            return moList

def main():
    print("Mean of [1, 3, 3, 4, 5, 5, 7, 8, 10, 10]: ", mean(list(range(1, 11))))
    print("Mode of [2, 1, 2, 2, 4, 4]:", mode([2, 1, 2, 2, 4, 4,]))
    print("Median of [1, 3, 3, 4]:". median([1, 3, 3, 4])))

mmain()
