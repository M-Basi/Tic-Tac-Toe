import clear

# row_dict = {
#     "1": [" ", "|", " ", "|", " "],
#     "2": [" ", "|", " ", "|", " "],
#     "3": [" ", "|", " ", "|", " "],
# }

line = "_____"
empty = " "

def tic_print():
    row = ["".join(row_dict[key]) for key in row_dict]
    for n in range(len(row)):
        if n== 2:
            print(row[n])
        else:
            print(row[n])
            print(line)




def win(symbol):
    number = 0
    if symbol == "0":
        won_player = 1
    else:
        won_player = 2
    for key in row_dict:
        if row_dict[key][0] == row_dict[key][2] == row_dict[key][4] == symbol:
            print(f"Player {won_player} won. Game Over")
            number =1
    for n in range(0,5,2):
        if row_dict["1"][n]==row_dict["2"][n]==row_dict["3"][n] == symbol:
            print(f"Player {won_player} won. Game Over")
            number = 1
    if row_dict["1"][0] == row_dict["2"][2] == row_dict["3"][4] == symbol:
        print(f"Player {won_player} won. Game Over")
        number =1
    elif row_dict["3"][0] == row_dict["2"][2] == row_dict["1"][4] == symbol:
        print(f"Player {won_player} won. Game Over")
        number = 1
    if number==0:
        return True
    else:
        return False

def more_moves():
    empty = " "
    if empty in row_dict["1"] or empty in row_dict["2"] or empty in row_dict["3"]:
        return True
    else:
        print("He have a draw. Nobody won")
        return False

def empty_cell(user_choice):
    if user_choice == empty:
        return True
    else:
        print("Not empty cell. Try again")
        tic_print()
        return False





def play_game():
    game_is_not_over = True

    print("1st player has 0 and 2nd player has X")
    tic_print()
    while game_is_not_over:
        for n in range(0,2):
            empty = " "
            if game_is_not_over:
                if n==0:
                    symbol = "0"
                else:
                    symbol = "X"
                user_row = input(f"Player No {n+1} please choose a row between 1 to 3: ")
                user_column = int(input(f"Player No {n+1} please choose a column between 1 to 3: "))
                changed_row = row_dict[user_row][(user_column - 1) * 2]
                while not empty_cell(changed_row):
                    user_row = input(f"Player No {n + 1} please choose a row between 1 to 3: ")
                    user_column = int(input(f"Player No {n + 1} please choose a column between 1 to 3: "))
                    changed_row = row_dict[user_row][(user_column - 1) * 2]
                row_dict[user_row][(user_column-1)*2] = symbol
                tic_print()
                if not win(symbol) or not more_moves():
                    game_is_not_over = False




while input("Do you want to play a game of Tic Tac Toe? Type 'y' or 'n':  ") == "y":
    clear.clear()
    row_dict = {
        "1": [" ", "|", " ", "|", " "],
        "2": [" ", "|", " ", "|", " "],
        "3": [" ", "|", " ", "|", " "],
    }
    play_game()



