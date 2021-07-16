def main():

    nested_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name, score])

    lowest_grade = min(nested_list[0][1], nested_list[1][1])
    second_lowest = max(nested_list[0][1], nested_list[1][1])

    for list in nested_list:

        for grade in list:

            check_float = isinstance(grade, float)

            if check_float == True:

                if lowest_grade > grade:
                    second_lowest = lowest_grade
                    lowest_grade = grade

    students_second_lowest = []

    for list in nested_list:

        grade = list[1]

        if grade == second_lowest:

            for name in list:

                check_str = isinstance(name, str)

                if check_str == True:

                    students_second_lowest.append(name)

    students_second_lowest.sort()

    for student in students_second_lowest:

        print(student)

if __name__ == '__main__':
    main()
