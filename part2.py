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

rights = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]


result_trees = 1
for right, down in zip(rights, down):
    result_trees *= calculate_trees(input_file, right, down)

print(result_trees)