with open("input.txt", "r") as f:
    input_file = [x.rstrip("\n") for x in f.readlines()]

copied_input = input_file


def calculate_trees(input_file, right, down):
    row_len = len(input_file)
    column_len = len(input_file[0])

    x = 0
    treecounter = 0
    for y in range(down, row_len, down):
        x += right
        mod_x = x % column_len
        if input_file[y][mod_x] == "#":
            treecounter += 1

    return treecounter

print(calculate_trees(input_file, 3, 1))

