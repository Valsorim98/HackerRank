from random import randrange

def main():

    n = int(input())
    A = []

    for num in range(n):
        rand = randrange(-100, 100)
        A.append(rand)

    print(A)

    maximum = max(A[0], A[1])
    second_max = min(A[0], A[1])

    for i in range(n):
        if A[i] > maximum:
            second_max = maximum
            maximum = A[i]

        if A[i] < maximum and A[i] > second_max:
            second_max = A[i]

    print(second_max)

if __name__ == "__main__":
    main()
