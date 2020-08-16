#Circle and cross game

#Pseudocode

#Show game instructions
#Figure out who's turn is this
#Create empty game table
#Show table
#While no one win
    #If its human move
        #Read human move
        #Update move on the game table
    #Else
        #Make computer move
        #Update move on the game table
    #Show the table
    #Change move maker

#Constant
NUM_SQUARE = ("0","1","2","3","4","5","6","7","8")
EMPTY = " "
TIE = "TIE"
X = "X"
O = "O"

#Functions
def display_instructions():
    print("""
Witaj w grze w kółko i krzyżyk. Zasady są ogólnie znane - na przemian z komputerem wstawiasz kółko lub krzyżyk
na planszy 3x3. Wygrywa ten, kto jako pierwszy ustawi swoje trzy znaki w lini poziomej, pionowej lub po skosie.
Plansza do gry wygląda następująco :

                            0 | 1 | 2
                           -----------
                            3 | 4 | 5
                           -----------
                            6 | 7 | 8

Liczby oznaczają konkretne pozycje, w które możesz wstawić swój znak - krzyżyk.
Aby to zrobić wpisz liczbę wybranego przez Ciebie pola.
Powodzenia ! """)

def yes_no_question(question):
    """Ask if user wants make first move. Reutrn 'tak' or 'nie'"""
    whos_move = None
    anwser = None
    while anwser not in ("tak","nie"):
        anwser = input(question)
        anwser = anwser.lower()
    return anwser

def first_turn_question():
    """Returns 'human (X)' or 'computer (O)'"""
    turn = None
    anwser = yes_no_question("Czy chcesz wykonać ruch jako pierwszy ? (tak/nie)\n")
    if anwser == "tak":
        turn = X
    elif anwser == "nie":
        turn == O
    return turn

def new_board():
    """Creates 3x3 empty, modyficable game table, input number, output game table with X or O"""
    board =[]
    for position in range(9):
        board.append(EMPTY)
    return board

def show_board(board):
    """Shows game table"""
    print("\n\t\t\t",board[0],"|",board[1],"|",board[2],"\t\t\t  0 | 1 | 2")
    print("\t\t\t","---------","\t\t\t -----------")
    print("\t\t\t",board[3],"|",board[4],"|",board[5],"\t\t\t  3 | 4 | 5")
    print("\t\t\t","---------","\t\t\t -----------")
    print("\t\t\t",board[6],"|",board[7],"|",board[8],"\t\t\t  6 | 7 | 8")
    
def move_ask(board):
    """Asking about square number, returns that number"""
    number = None
    while True:
        number = input("\nGdzie chcesz zrobić ruch ? (0-8)")
        if number in NUM_SQUARE:
            number = int(number)
            if number in legal_moves(board):
                return number
            else:
                print("Nie możesz wykonać tego ruchu...")
                continue
        else:
            continue
   

    
def winner(board):
    """Input - game_table, returns none when no one wins, computer(O) or human(X) or TIE"""
    WAYS_WIN = ((0,1,2),
                (3,4,5),
                (6,7,8),
                (0,3,6),
                (1,4,7),
                (2,5,8),
                (0,4,8),
                (2,4,6))
    winner = None
    for position in WAYS_WIN:
        if board[position[0]] == board[position[1]] == board[position[2]] != EMPTY:
            winner = board[position[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def legal_moves(board):
    """Input board, returns list of aviable moves"""
    legal_moves = []
    for row in range(9):
        if board[row] == EMPTY:
            legal_moves.append(row)
    return legal_moves

def computer_move(board):
    """Input board, returns number, position on board"""
    #If computer can win, make that move
        #Create copy of game board
        #Make all of available moves on copy
        #If any move gives win, make it
    test_board = board[:]
    av_moves = legal_moves(test_board)
    for move in av_moves:
        test_board[move] = O
        if winner(test_board) == O:
            return move
        test_board[move] = EMPTY

    #If player can win, block
        #Check all aviable human moves
        #If any move gives human win, make that move as computer   
    for move in av_moves:
        test_board[move] = X
        if winner(test_board) == X:
              return move 
        test_board[move] = EMPTY      
    #Else make move in order (4, 0, 2, 6, 8, 3, 1, 5, 7) - make move if can ofc
    BEST_MOVES = (4, 0, 2, 6, 8, 3, 1, 5, 7)
    for move in BEST_MOVES:
        if move in av_moves:
            return move

def turn_change(turn):
    """Input current turn, returns oposite player turn"""
    if turn == X:
        turn = O
    else:
        turn = X
    return turn

#MAIN+INTRO
def main_intro():
    #Print instructions
    display_instructions()
#MAIN
def main():
    #Whos first turn
    turn = first_turn_question()

    #Creates new, empty board
    current_board = new_board()

    #While loop
    while winner(current_board) == None:
        if turn == X:
            human_move = move_ask(current_board)
            current_board[human_move] = X
            print("Twój ruch...")
        else:
            comp_move = computer_move(current_board)
            current_board[comp_move] = O
            print("Mój ruch...")

        show_board(current_board)
        turn = turn_change(turn)

    #Gratulations / game over
    if winner(current_board) == X:
        print("\nGratuluję! Udało Ci się pokonać komputer w tej zaciekłej walce")
    elif winner(current_board) == TIE:
        print("Remis...")
    else:
        print("\nNiestety, komputer okazał się lepszy od Ciebie...")

#Again?
main_intro()
again = None 
while True:
    main()
    again = yes_no_question("\nCzy chcesz zacząć od nowa ? (tak/nie)\n")
    if again == "nie":
        break
    else:
        continue
#Ending
input("Wciśnij ENTER, żeby zakończyć...")
    
    














