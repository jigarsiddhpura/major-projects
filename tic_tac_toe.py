
def Board(xState, oState):
    '''Board func refreshes the game board with the user input'''
    # Ternary operators are used below
    # If value at a perticular index is 1 , X/O is printed  at the index 
    # depending on the list where it is 1
    zero = 'X' if xState[0] else ('O' if oState[0] else 0)
    one = 'X' if xState[1] else ('O' if oState[1] else 1)
    two = 'X' if xState[2] else ('O' if oState[2] else 2)
    three = 'X' if xState[3] else ('O' if oState[3] else 3)
    four = 'X' if xState[4] else ('O' if oState[4] else 4)
    five = 'X' if xState[5] else ('O' if oState[5] else 5)
    six = 'X' if xState[6] else ('O' if oState[6] else 6)
    seven = 'X' if xState[7] else ('O' if oState[7] else 7)
    eight = 'X' if xState[8] else ('O' if oState[8] else 8)

    print(f'{zero} | {one} | {two}')
    print(f'--|---|--')
    print(f'{three} | {four} | {five}')
    print(f'--|---|--')
    print(f'{six} | {seven} | {eight}')

def sum(a, b, c):
    return a+b+c

def checkwin(xState, oState):
    '''checkwins return 0/1 according to the winner(O/X) else return -1'''
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
        0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8]]
    for i in wins:
        if sum(xState[i[0]], xState[i[1]], xState[i[2]]) == 3:
            print('X Wins !!!')
            return 1
        if sum(oState[i[0]], oState[i[1]], oState[i[2]]) == 3:
            print('O Wins !!!')
            return 0
    return -1


if __name__ == '__main__':
    while(1):
        # Changes r done in the below lists acc to the input of user
        #  0 -> 1 is done at the index (value) in the lists below
        xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        oState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # 1 for X & 0 for O
        turn = 1
        print('Tic Tac Toe Game ')
        while(1):
            Board(xState, oState)
            if turn == 1:
                print("X's chance")
                value = int(input('Where do u wanna enter X ? '))
                xState[value] = 1
            else:
                print("O's chance")
                value = int(input('Where do u wanna enter O ? '))
                oState[value] = 1

            cwin = checkwin(xState, oState)
            if cwin != -1:
                print('GAME OVER')
                break

            # Below line changes turn 0 -> 1 or 1 -> 0 everytime
            turn = 1 - turn
        restart = input("Enter 'yes' play again otherwise Press any key\n")
        if restart != 'yes':
            break