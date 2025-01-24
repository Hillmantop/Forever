
#your project’s title: Tic Tac Toe
#your name: Mzingisi Ndamase
#Github :Hillmantop    
# edx: Mzingisi
# city and country: Margate, South Africa
#the date you have recorded this video: 28 May 2024


# To store the X's and O's game we need a board

board = [ ' ' for x in range(10)] # a list, creates ten empty spaces using a list comprehension
#board  = [' ', 'X','O','O',' ',' ',' ',' ',' ',' ']
# The player inserts a letter into the board list
def insertLetter(letter, positon):
    board[positon]= letter
    
def reset_board(board):
    return [' ' for x in range(10)]

# check if the  space the user would like to iinsert into is free 
def isSpaceFree(positon):
    return board[positon] == ' '

# print the board
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | '+ board[2]+ ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | '+ board[5]+ ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | '+ board[8]+ ' | ' + board[9])
    print('   |   |') #
    
    
#Checks if there is  a winner based on the current board
def isWinner(bo, le):       #bo- board, le-letter
    
    #check the rows then the diagonals then the columns
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

# insert a X in the location the player chooses
def playerMove():#  reading here
    run = True
    while run:
        move = input('Please select a position to place an X (1-9): ')  
        try:
            #error checking the input
            move = int(move)
            if move > 0 and move < 10:
                #check to see if the space is free
                if isSpaceFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range')
                    
        except:
            print('Please type a number')
            
def player1Move(player):
    run = True
    while run:
        move = input(f'Player {player} please select a position (1-9): ')
        try:
            #error handling
            move = int(move)
            if move > 0 and move < 10:
                #check to see if the space is free
                if isSpaceFree(move):
                    run = False
                
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range')
        
        except:
            print('Please type a number')
            
def player2Move(player):
    run = True
    while run:
        move = input(f'Player {player} please select a position (1-9): ')
        try:
            #error handling
            move = int(move)
            if move > 0 and move < 10:
                #check to see if the space in free
                if isSpaceFree(move):
                    run = False
                    insertLetter('O', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range')
                
        except:
            print('Please type a number')
            
            
                
                    
        
# Computers move, this says which index the computer can move to 
def compMove():
    
    #generate a new list of index values from the current board where there are empty spaces and dont inclue the zeroth index in the list
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    
    #check if the player can win then we check if the computer can win(in other words are we one move away from winning), X for player and O for computer in the outer loop
    for letter in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = letter
            if isWinner(boardCopy, letter):#  
                move = i
                return move
    
         
    #check if any corners are open in the original board, if there any we choose a random one to move the O into.   
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    #select , at random, which corner to move into
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
        
        
    #check the center is open
    if 5 in possibleMoves:
        move = 5
        return move
    
    #check the edges
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    #select , at random, which edge to move into
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move
    
    return move

# select a random move
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln) #has to start from 0 to ln because we are using the index values
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
    
def multiplayer():
    multiplayer =int(input("Select 1 to play against Ai or 2 for multiplayer: "))
    printBoard(board)
    
    
    #check if multiplayer is 1, then start the code for single player if not code for 2
    
    if multiplayer == 1: #  at running the multipllayer code with the debugger for interests sake 
        #single player against AI
        while not(isBoardFull(board)): 
            #check if computer has won
            if not(isWinner(board, 'O')):
                playerMove()
                printBoard(board)
                
            # if computer has won
            else:
                print('Sorry,  Os has won this time')
                break #to get out of the while loop
            
            
            #check if player has won, if not insert O for computer
            if not(isWinner(board, 'X')):
                move = compMove()
                
                #check to see if there was a move made through compMove, check for a tie game
                if move != 0:
                    insertLetter('O', move)
                    print('Computer placed an \'O\' in position', move , ':')
                    printBoard(board)
                
                
                    
            # if player hasnt won
            else:
                print('The Xs have won this time, Well done')
                break #to get out of the while loop
                
        
        #checks for the end of the game
        if isBoardFull(board):
            print('Game is a tie! No more spaces left to move.')
    
    #multiplayer , two players taking turns. 
    if multiplayer == 2: 
        #this block will have two players
        #player 1 is X and 2 is O
        
       
        
        
        while not(isBoardFull(board)):
            #player 1 makes a move with X
            
            # check if player 1(X) has won 
            if  not(isWinner(board, 'O')):
                #player 1 makes a move
                player1 = 'X'
                player1Move(player1) #this just inserts O into the location chosen
                printBoard(board)
                
            else: 
                print('Os Wins')
                break
                
            # check if player 2(O) has won  
            if  not(isWinner(board, 'X')):
                #player 2 makes a move
                player2 = "O"
                player2Move(player2) 
                printBoard(board)
            
            else: 
                print('Xs Wins')
                break
                    
                    
                    
            
        
                
        
def main():
    multiplayer()
    
    
#implementing an option to restart the game

#check if the game is over(fullboard or either player has won) , if over ask if user wants to restart else just run the game as usual
while not(isBoardFull(board)) or not(isWinner(board, 'O')) or not(isWinner(board, 'X')):
    
    #check for full board, so we can  start a new game
    if isBoardFull(board) == True:
        turn = input('Would you like to play again?yes or no: ')
        if turn == 'yes':
            board = reset_board(board) # to clear the board of any Xs or Os
            main()
        else:
            break
    
    #check if O win,
    elif isWinner(board, 'O') == True:
        turn1 = input('Would you like to play again?yes or no: ')
        if turn1 == 'yes':
            board = reset_board(board)
            main()
        else:
            break
        
    #check if X wins
    elif isWinner(board, 'X') == True:
        turn2 = input('Would you like to play again?yes or no: ')
        if turn2 == 'yes':
            board = reset_board(board)
            main()
        else:
            break
    
    # the game is new so just play
    else:
        main()
        
    
            
            
   
   
                  
            
        
                
        
                
        
                
        
        
        
        
            
            
                
            
            


#we know a game is over when there is either a tie or player 1 has won or player 2 has won in multiplayer
    
   
    
    
    
    
