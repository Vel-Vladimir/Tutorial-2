from random import randint
from time import sleep
SIZE_COL = 3
SIZE_ROW = 4
level_count = 1
def draw_field(user_row, user_col, EXIT_ROW, EXIT_COL, SIZE_ROW, SIZE_COL):
    global level_count
    line= ""
    if user_row == EXIT_ROW and user_col == EXIT_COL:
        print("            *** Congratulation!! You're a winner!!'. ***")
        level_count += 1
        print(f"                 *** Level №{level_count}***")
        sleep(3)
        is_next_level = True
        return is_next_level
    for r in range(SIZE_ROW):
        line += "|"
        for c in range(SIZE_COL):
            if r == user_row and c == user_col:
                line += "*|"
                continue
            
            elif r == EXIT_ROW and c == EXIT_COL:
                line += "x|"
                continue
            line +=" |"
        line += "\n"
    print(line)
    
def position_player_exit(SIZE_COL, SIZE_ROW):
    EXIT_COL = randint(0, SIZE_COL - 1)  # coordinate of exit door starting from 0
    EXIT_ROW = randint(0, SIZE_ROW - 1)  # coordinate of exit door starting from 0
    cur_row = randint(0, SIZE_ROW - 1) 
    cur_col = randint(0, SIZE_COL - 1) 
    return (cur_row, cur_col, EXIT_ROW, EXIT_COL)

cur_row, cur_col, EXIT_ROW, EXIT_COL = position_player_exit(SIZE_COL, SIZE_ROW)
draw_field(cur_row, cur_col, EXIT_ROW, EXIT_COL, SIZE_ROW, SIZE_COL)

while True:
    move = input("Enter direction: (l/r/u/d) ")
    if move == "l":
                
        if cur_col > 0:
            cur_col -= 1
        is_next_level = draw_field(cur_row, cur_col, EXIT_ROW, EXIT_COL, SIZE_ROW, SIZE_COL)
        
    elif move == "r":
                
        if cur_col < SIZE_COL - 1:
            cur_col += 1        
        is_next_level = draw_field(cur_row, cur_col, EXIT_ROW, EXIT_COL, SIZE_ROW, SIZE_COL)

    elif move == "u":
        
        if cur_row > 0:
            cur_row -= 1
        is_next_level = draw_field(cur_row, cur_col, EXIT_ROW, EXIT_COL, SIZE_ROW, SIZE_COL)

    elif move == "d":
                
        if cur_row < SIZE_ROW - 1:
            cur_row += 1
        is_next_level = draw_field(cur_row, cur_col, EXIT_ROW, EXIT_COL, SIZE_ROW, SIZE_COL)
        
    elif move == "e":
        break
    else:

        print("Wrong direction. Enter right direction")
    
    if is_next_level:
        SIZE_COL += 2
        SIZE_ROW += 2
        cur_row, cur_col, EXIT_ROW, EXIT_COL = position_player_exit(SIZE_COL, SIZE_ROW)
        draw_field(cur_row, cur_col, EXIT_ROW, EXIT_COL, SIZE_ROW, SIZE_COL)



