def arithmetic_arranger(problems, do_math=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_operands, bottom_operands, operators = [], [], []
    
    for problem in problems:
        li = problem.split(' ')
        top_operands.append(li[0])
        bottom_operands.append(li[2])
        operators.append(li[1])

    if '*' in operators or '/' in operators:
        return "Error: Operator must be '+' or '-'."

    for i in range(len(top_operands)):
        if not top_operands[i].isdigit() or not bottom_operands[i].isdigit():
            return "Error: Numbers must only contain digits."
        if len(top_operands[i]) > 4 or len(bottom_operands[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    answers = []

    if do_math:
        for i in range(len(operators)):
            if operators[i] == '+':
                answers.append(str(int(top_operands[i]) + int(bottom_operands[i])))
            else:
                answers.append(str(int(top_operands[i]) - int(bottom_operands[i])))

            if len(answers[i]) > max(len(top_operands[i]), len(bottom_operands[i])):
                answers[i] = ' ' + answers[i]
            else:
                answers[i] = ' ' * (max(len(top_operands[i]), len(bottom_operands[i])) - len(answers[i]) + 2) + answers[i]

    seperators = []

    for i in range(len(top_operands)):
        if len(top_operands[i]) > len(bottom_operands[i]):
            top_operands[i] = (' ' * 2) + top_operands[i]
            bottom_operands[i] = operators[i] + (' ' * (len(top_operands[i]) - len(bottom_operands[i]) - 1)) + bottom_operands[i]
            seperators.append('-' * len(top_operands[i]))
        else:
            top_operands[i] = (' ' * (len(bottom_operands[i]) - len(top_operands[i]) + 2)) + top_operands[i]
            bottom_operands[i] = operators[i] + ' ' + bottom_operands[i]
            seperators.append('-' * len(top_operands[i]))

    if do_math:
        arranged_problems = "    ".join(top_operands) + "\n" + '    '.join(bottom_operands) + '\n' + "    ".join(seperators) + '\n' + "    ".join(answers)
    else:
        arranged_problems = "    ".join(top_operands) + '\n' + '    '.join(bottom_operands) + '\n' + '    '.join(seperators)

    return arranged_problems
