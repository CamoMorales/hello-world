file = input("Enter the input file name: ")
f = open(file, 'r')
l = list(f.readlines())
for i in range(len(1)):
    l[i]=1[i][:-1]
numbers = []
for i in l:
    temp = i.split(" ")
    for j in temp:
        numbers.append(int(j))
print("The average is", sum(numbers)/len(numbers))
