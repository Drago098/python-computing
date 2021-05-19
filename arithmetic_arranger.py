def arithmetic_arranger(problems, display=False):
    
    operators = []
    longest_operands = []
    len_diffs = []

    num_spaces = []

    print_list = []
    print_list_2 = []
    print_list_3 = []

    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in range(len(problems)):
        if "+" in problems[problem]:
            problems[problem] = problems[problem].split(" + ")
            operators.append("+")
            
        elif "-" in problems[problem]:
            problems[problem] = problems[problem].split(" - ")
            operators.append("-")

        else:
            return "Error: Operator must be '+' or '-'."

    for problem in range(len(problems)):
        if problems[problem][0].isdigit() == False:
            return "Error: Numbers must only contain digits."
        elif problems[problem][1].isdigit() == False:
            return "Error: Numbers must only contain digits."

    for problem in range(len(problems)):
        if len(problems[problem][0]) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif len(problems[problem][1]) > 4:
            return "Error: Numbers cannot be more than four digits."

    for problem in range(len(problems)):
        if len(problems[problem][0]) < len(problems[problem][1]):
            longest_operands.append("1")

            len_diffs.append(1 + (len(problems[problem][1])-len(problems[problem][0])))
        else:
            longest_operands.append("-1")

            len_diffs.append(-1 - (len(problems[problem][0])-len(problems[problem][1])))

    #---------------------------------

    for lens in range(len(len_diffs)):
        if len_diffs[lens] > 0:
            for num_times_print in range(len_diffs[lens]):
                print_list.append(" ")
            print_list.append(" ")
            print_list.append(problems[lens][0])

            if lens != (len(problems) - 1):
                print_list.append("    ")
        else:
            print_list.append("  ")
            print_list.append(problems[lens][0])

            if lens != (len(problems) - 1):
                print_list.append("    ")

    for lens in range(len(len_diffs)):
        print_list_2.append(operators[lens])
        if len_diffs[lens] < 0:
            for spaces in range(abs(len_diffs[lens])):
                print_list_2.append(" ")
            print_list_2.append(problems[lens][1])

            if lens != (len(problems) - 1):
                print_list_2.append("    ")
        else:
            print_list_2.append(" ")
            print_list_2.append(problems[lens][1])

            if lens != (len(problems) - 1):
                print_list_2.append("    ")

    for operands in range(len(longest_operands)):
        if longest_operands[operands] == "-1":
            for number_of_dashes in range(len(problems[operands][0])+2):
                print_list_3.append("-")
        else:
            for number_of_dashes in range(len(problems[operands][1])+2):
                print_list_3.append("-")
                

        if operands != (len(problems) - 1):
            print_list_3.append("    ")

    return_statement = ''.join(print_list) + "\n" + ''.join(print_list_2) + "\n" + ''.join(print_list_3)
    
    if display == True:
        solutions = []
        print_list_4 = []
        for problem in range(len(problems)):
            if operators[problem] == "+":
                solutions.append(int(problems[problem][0]) + int(problems[problem][1]))
            else:
                solutions.append(int(problems[problem][0]) - int(problems[problem][1]))

        for problem in range(len(problems)):
            if len(problems[problem][0]) > len(problems[problem][1]):
                num_spaces.append(len(str(problems[problem][0])) - len(str(solutions[problem])))
            else:
                num_spaces.append(len(str(problems[problem][1])) - len(str(solutions[problem])))

        for spaces in range(len(num_spaces)):
            for i in range(2 + int(num_spaces[spaces])):
                print_list_4.append(" ")
                
            print_list_4.append(solutions[spaces])

            if spaces != (len(problems) - 1):
                print_list_4.append("    ")

        for i in range(len(print_list_4)):
            if isinstance(print_list_4[i], int):
                print_list_4[i] = str(print_list_4[i])

        return_statement = ''.join(print_list) + "\n" + ''.join(print_list_2) + "\n" + ''.join(print_list_3) + "\n" + ''.join(print_list_4)
            
        return return_statement

    else:
        return return_statement
