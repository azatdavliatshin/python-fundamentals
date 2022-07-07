### Task 2.8
# Write a program which makes a pretty print of a part of the multiplication table.
# Examples:
#
# Input:
# a = 2
# b = 4
# c = 3
# d = 7

# Output:
#	    3	4	5	6	7	
#   2	6	8	10	12	14	
#   3	9	12	15	18	21	
#   4	12	16	20	24	28


def execute_task():
    print("a program which makes a pretty print of a part of the multiplication table\n");
    a = int(input(("Enter start row\n")));
    b = int(input(("Enter end row\n")));
    c = int(input(("Enter start column\n")));
    d = int(input(("Enter end column\n")));
    print("Output is \n{}\n".format(pretty_print_matrix(a,b,c,d)));

def pretty_print_matrix(a,b,c,d):
    rows = [''] + [digit for digit in range(a, b + 1)]
    columns = [''] + [digit for digit in range(c, d + 1)]
    matrix = []

    for idrow, row in enumerate(rows):
        if idrow == 0:
            matrix.append(columns);
        else:
            new_row = [];
            for idcolumn, column in enumerate(columns):
                if idcolumn == 0:
                    new_row.append(row)
                else:
                    new_row.append(row * column)
            matrix.append(new_row)

    return '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]);