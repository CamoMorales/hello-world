import math

tolerance = 0.000001

def newton(n):
    estimate = 1.0
    while True:
        estimate = (estimate + n / estimate) / 2
        root = abs(n - estimate ** 2)
        if root <= tolerance:
            break

    return estimate

def main():
    while True:
        number = input("Enter positive number / enter to exit: ")
        if number - "":
            break
        number = float(number)
        estimate = newton(number)

        print("The program's estimate is ", estimate)
        print("Python's estimate is ", math.sqrt(number))

if __name__ == "__main__":
    main()
