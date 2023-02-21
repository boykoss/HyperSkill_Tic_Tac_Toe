data = "         "
field = [i for i in data]
shot = "X"
updated_field = [
        field[0:3],
        field[3:6],
        field[6:9]
]
print("---------")
print("| " + " ".join(updated_field[0]) + " |")
print("| " + " ".join(updated_field[1]) + " |")
print("| " + " ".join(updated_field[2]) + " |")
print("---------")

def check_condition(f, c):
        board = [item for group in f for item in group]
        xxx_gorizontal = (board[0] == board[1] == board[2] and board[0] == "X") or (
                        board[3] == board[4] == board[5] and board[3] == "X") or (
                                         board[6] == board[7] == board[8] and board[6] == "X")
        xxx_diagonal = (board[0] == board[4] == board[8] and board[0] == "X") or (
                        board[2] == board[4] == board[6] and board[2] == "X")
        xxx_vertical = (board[0] == board[3] == board[6] and board[0] == "X") or (
                        board[1] == board[4] == board[7] and board[1] == "X") or (
                                       board[2] == board[5] == board[8] and board[2] == "X")
        xxx_won = xxx_vertical or xxx_gorizontal or xxx_diagonal

        ooo_gorizontal = (board[0] == board[1] == board[2] and board[0] == "O") or (
                        board[3] == board[4] == board[5] and board[3] == "O") or (
                                         board[6] == board[7] == board[8] and board[6] == "O")
        ooo_diagonal = (board[0] == board[4] == board[8] and board[0]) == "O" or (
                        board[2] == board[4] == board[6] and board[2] == "O")
        ooo_vertical = (board[0] == board[3] == board[6] and board[0]) == "O" or (
                        board[1] == board[4] == board[7] and board[1] == "O") or (
                                       board[2] == board[5] == board[8] and board[2] == "O")
        ooo_won = ooo_vertical or ooo_gorizontal or ooo_diagonal

        there_ = board.__contains__(" ")

        if (xxx_won and ooo_won):
                print("Impossible")
        else:
                if xxx_won and not ooo_won:
                        print("X wins")

                elif ooo_won and not xxx_won:
                        print("O wins")
                elif not xxx_won and not ooo_won and not there_:
                        print("Draw")
                elif not xxx_won and not ooo_won and there_:
                        if c == "X":
                                c = "O"
                                start(c)
                        else:
                                c = "X"
                                start(c)

def start(coor):
        coordinates = input().split(" ")

        a = int(coordinates[0]) - 1
        b = int(coordinates[1]) - 1


        if not coordinates[0].isalpha() or not coordinates[1].isalpha():
                if (int(coordinates[0]) in range(0, 4) and int(coordinates[1]) in range(0, 4)):
                        if updated_field[a][b].isspace():
                                updated_field[a][b] = coor
                                print("---------")
                                print("| " + " ".join(updated_field[0]) + " |")
                                print("| " + " ".join(updated_field[1]) + " |")
                                print("| " + " ".join(updated_field[2]) + " |")
                                print("---------")


                                check_condition(updated_field, coor)
                        else:
                                print("This cell is occupied! Choose another one!")
                                start(coor)
                else:
                        print("Coordinates should be from 1 to 3!")
                        start(coor)

        else:
                print("You should enter numbers!")
                start(coor)
start(shot)









