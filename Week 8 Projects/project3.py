import math

tolerance = 0.000001

def newton(x, estimate):
    estimate = (estimate + x / estimate) / 2
    root = abs(x - tolerance ** 2)
    if root <= tolerance:
        return estimate
    else:
        return newton(x, (estimate + x / estimate) / 2)

def main():
    while True:
        x = input("Enter positive number / enter to exit: ")
        if x == "":
            break
        x = float(x)
        estimate = 1.0
        print("The program's estimate is", newton(x,estimate))
        print("Python's estimate is ", math.sqrt(x))

if __name__ == "__main__":
    main()
