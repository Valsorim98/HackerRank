from collections import Counter

def main():

    arr = []

    print("Please input 5 integers.")

    for number in range (5):

        x = int(input())
        arr.append(x)

    print(f"Array: {arr}")

    print(f"Here are the first three numbers from the array: {arr[0]}, {arr[1]}, {arr[2]}")

    # To count how many times the elements are repeated in the array.
    repetitives = dict(Counter(arr))

    print(f"Repeated elements: {repetitives}")

    # Get the most repeated element.
    max_value = max(repetitives, key=repetitives.get)

    print(f"Most repeated element is: {max_value}")

    # Extend the array with itself.
    # arr.extend(arr)

    # Print the array in reverse order.
    print(list(reversed(arr)))

if __name__ == "__main__":
    main()
