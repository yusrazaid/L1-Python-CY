print("This is my holi/womens day tic tac toe game")
print("W for national womens day and H for holi")
print("W goes first then H goes next")
print("Here is a guide to the grid\n1 2 3\n4 5 6\n7 8 9")
board=[" " for i in range(9)]
def print_board():
    row1="| {} | {} | {} |".format(board[0], board[1], board[2])
    row2="| {} | {} | {} |".format(board[3], board[4], board[5])
    row3="| {} | {} | {} |".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon=="W":
        number=1
    elif icon=="H":
        number=2
    print("Your turn player {}".format(number))
    choice=int(input("Enter your move (1-9:) ").strip())
    if board[choice -1]==" ":
        board[choice -1]=icon
    else:
        print()
        print("That space is taken")
def is_victory(icon):
    if  (board[0]==icon and board[1]==icon and board[2]==icon)or\
        (board[3]==icon and board[4]==icon and board[5]==icon)or\
        (board[6]==icon and board[7]==icon and board[8]==icon)or\
        (board[0]==icon and board[3]==icon and board[6]==icon)or\
        (board[1]==icon and board[4]==icon and board[7]==icon)or\
        (board[2]==icon and board[5]==icon and board[8]==icon)or\
        (board[0]==icon and board[4]==icon and board[8]==icon)or\
        (board[2]==icon and board[4]==icon and board[6]==icon):
         return True   
    else:
        return False
def is_draw():
    if " " not in board:
         return True
    else:
        return False
     
    
while True:
    print_board()
    player_move("W")
    print_board()
    if is_victory("W"):
        print("W wins happy womens day! :D")
        break
    elif is_draw():
        print("It's a draw!\nHappy Holi\nHappy Womens day")
        break
    player_move("H")
    if is_victory("H"):
        print_board()
        print("H wins happy Holi! :D")
        break
   
    
   
