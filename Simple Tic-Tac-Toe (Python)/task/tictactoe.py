data = input()


field = [i for i in data]

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

while True:

        coordinates = input().split(" ")

        a = int(coordinates[0]) - 1
        b = int(coordinates[1]) - 1

        if not coordinates[0].isalpha() or not coordinates[1].isalpha():
                if (int(coordinates[0]) in range(0, 4) and int(coordinates[1]) in range(0, 4)):
                        if updated_field[a][b] == "_":
                                updated_field[a][b] = "X"
                                print("---------")
                                print("| " + " ".join(updated_field[0]) + " |")
                                print("| " + " ".join(updated_field[1]) + " |")
                                print("| " + " ".join(updated_field[2]) + " |")
                                print("---------")
                                exit()
                        else:
                                print("This cell is occupied! Choose another one!")
                else:
                        print("Coordinates should be from 1 to 3!")

        else:
                print("You should enter numbers!")








#
# x = 0
# o = 0
# for i in "".join(field):
#         if i == "X":
#                 x += 1
#         elif i == "O":
#                 o += 1
#
#
# xxx_gorizontal = (field[0] == field[1] == field[2] and field[0] == "X") or (field[3] == field[4] == field[5] and field[3] == "X") or (field[6] == field[7] == field[8] and field[6] == "X")
# xxx_diagonal = (field[0] == field[4] == field[8] and field[0] == "X") or (field[2] == field[4] == field[6] and field[2] == "X")
# xxx_vertical = (field[0] == field[3] == field[6] and field[0] == "X") or (field[1] == field[4] == field[7] and field[1] == "X") or (field[2] == field[5] == field[8] and field[2] == "X")
# xxx_won = xxx_vertical or xxx_gorizontal or xxx_diagonal
#
# ooo_gorizontal = (field[0] == field[1] == field[2] and field[0] == "O") or (field[3] == field[4] == field[5] and field[3] == "O") or (field[6] == field[7] == field[8] and field[6] == "O")
# ooo_diagonal = (field[0] == field[4] == field[8] and field[0]) == "O" or (field[2] == field[4] == field[6] and field[2] == "O")
# ooo_vertical = (field[0] == field[3] == field[6] and field[0]) == "O" or (field[1] == field[4] == field[7] and field[1] == "O") or (field[2] == field[5] == field[8] and field[2] == "O")
# ooo_won = ooo_vertical or ooo_gorizontal or ooo_diagonal
#
# there_ = field.__contains__("_")
#
#
# if (xxx_won and ooo_won) or (x - o >= 2 or o - x >= 2):
#         print("Impossible")
# else:
#         if xxx_won and not ooo_won:
#                 print("X wins")
#         elif ooo_won and not xxx_won:
#                 print("O wins")
#         elif not xxx_won and not ooo_won and there_:
#                 print("Game not finished")
#         elif not xxx_won and not ooo_won and not there_:
#                 print("Draw")





