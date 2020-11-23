#Crear el tablero
#Asignar jugadores
#Escoger jugador
#Mostrar el tablero
#Encontrar ganador
  #Mostrar el tablero
  #Seleccionar ubicacion
  #Mostrar jugador activo
#Terminar el juego

board = [
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-']
]

players = ["R", "B"]
players_index = 0
players_name = ['Player 1', 'Player 2']

def show_board(board):
    for row in range(6):
        print('|', end=' ')
        for posicion in range(7):
            print(board[row][posicion], end=' | ')
        print()

def active_player():
    global players_index
    turn = players_index % 2
    players_index += 1
    if turn == 0:
        print(f'{players_name[turn]} is your turn, Please choose a column between 0 and 6')
    else:
        print(f'{players_name[turn]} is your turn, Please choose a column between 0 and 6')
    return turn

def play_game():
    while True:
        turn = active_player()
        position = int(input('Choose a column: '))
        if position >= 7 or position < 0:
            print('Please choose a valid option')
        else:
            for row in range(5, -1, -1):
                if board[row][position] is not '_':
                    continue
                elif board[row][position] is '_':
                    board[row][position] = players[turn]
                    break
            show_board(boards)
            find_winner()

def find_winner():
    #4 fichas seguidas en una fila
    for player in range(0, 2):
        for column in range(0, 7):
            for column1 in range(0, 3):
                if board[column1][column] == players[active_player()] and board[column1 + 1][column] == players[active_player()] and board[column1 + 2][column] == players[active_player()] and board[column1 + 3][column] == players[active_player()]:
                    print(f'{player[active_player()]} Ganaste!')
                return players[active_player()]
    #4 fichas seguidas en una columna
    for player in range(0, 2):
        for column in range(0, 7):
            for column1 in range(0, 3):
                if board[column1][column] == players[active_player()] and board[column1][column + 1] == players[active_player()] and board[column1][column + 2] == players[active_player()] and board[column1][column + 3] == players[active_player()]:
                    print(f'{player[active_player()]} Ganaste!')
                return players[active_player()]
        #4 fichas seguidas en diagonal 


print('---------------------------')
print('         Connect_4       ')
print('---------------------------')

play_game()