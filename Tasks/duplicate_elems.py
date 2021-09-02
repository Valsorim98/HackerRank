import random

class Duplicates():

    def main():

        # Create two lists.
        original_array = []
        processed_array = []

        # Get ten random numbers from 0 to 9 and store them in original_array.
        for i in range(10):

            num = random.randrange(0,9)
            original_array.append(num)

        print(f"Original array: {original_array}")

        # Iterate through the original_array.
        for elem in original_array:

            # If processed_array is empty to store the first number from original_array in it.
            if len(processed_array) == 0:

                processed_array.append(original_array[0])

            # If the current element is not in processed_array to store it.
            if elem not in processed_array:

                processed_array.append(elem)

        print(f"Processed array: {processed_array}")

    if __name__ == "__main__":
        main()
