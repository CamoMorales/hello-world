def printAll(seq):
    print("Function argument: ", seq)
    if seq:
        print("In argument", seq, ", 1st letter is", seq[0])
        printAll(seq[1:])

printAll((1, 2, 3, 4))
printALL([1, 2, 3, 4])
printAll("Goodbye World!")
printAll("Good Morning America!")
