def right_justify(s):
    num_of_spaces = 70 - len(s)
    result = num_of_spaces * " " + s
    print(result)


right_justify("monty")
