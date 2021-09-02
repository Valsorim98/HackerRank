import random

def main():

    # Create a list.
    list_nums = []

    # While the length of the list is not 4, to get a new random number.
    while not len(list_nums) == 4:

        # The first number is from 1 to 9.
        x = random.randint(1, 9)

        if len(list_nums) >= 1:

            # Every other number is from 0 to 9.
            x = random.randint(0, 9)

        # If the random number is not in list_nums list to append it.
        if x not in list_nums:

            list_nums.append(x)

    print(f"The list: {list_nums}")

    str_num = ""

    for i in list_nums:
        
        str_num += str(i)

    # Print all the numbers from the list as one whole number.
    print(int(str_num))

if __name__ == "__main__":
    main()
