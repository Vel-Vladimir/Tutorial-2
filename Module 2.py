SIZE_COL = 3
SIZE_ROW = 4
EXIT_COL = 3
EXIT_ROW = 1

def draw_field(user_row, use_col, SIZE_ROW, SIZE_COL, EXIT_COL, EXIT_ROW):
    line= ""
    if user_row == EXIT_ROW and use_col == EXIT_COL:
        print("Congratulation. You won.")
        exit()
    for r in range(1, SIZE_ROW + 1):

        for c in range(1, SIZE_COL + 2):
            if r == user_row and c == use_col:
                line += "|*"
                continue
            
            if r == EXIT_ROW and c == EXIT_COL:
                line += "|x"
                continue
            line +="| "
        line += "\n"
    print(line)

cur_row = SIZE_ROW
cur_col = 1
draw_field(cur_row, cur_col, SIZE_ROW, SIZE_COL, EXIT_COL, EXIT_ROW)

playing = True
while playing:
    move = input("Enter direction: ")
    if move == "left":
        cur_col -= 1
        if cur_col > 0:
            draw_field(cur_row, cur_col, SIZE_ROW, SIZE_COL, EXIT_COL, EXIT_ROW)
        else:
            cur_col = 1
            draw_field(cur_row, cur_col, SIZE_ROW, SIZE_COL, EXIT_COL, EXIT_ROW)

    elif move == "right":
        cur_col += 1
        if cur_col <= SIZE_COL:
            draw_field(cur_row, cur_col, SIZE_ROW, SIZE_COL, EXIT_COL, EXIT_ROW)
        else:
            cur_col = SIZE_COL
            draw_field(cur_row, cur_col, SIZE_ROW, SIZE_COL, EXIT_COL, EXIT_ROW)

    elif move == "up":
        cur_row -= 1
        draw_field(cur_row, cur_col, SIZE_ROW, SIZE_COL, EXIT_COL, EXIT_ROW)
    elif move == "down":
        cur_row += 1
        draw_field(cur_row, cur_col, SIZE_ROW, SIZE_COL, EXIT_COL, EXIT_ROW)
    elif move == "exit":
        break
    else:
        print("Wrong direction. Enter right direction")
