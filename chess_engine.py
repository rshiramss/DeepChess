import chess.engine

# create a Stockfish engine object
engine = chess.engine.SimpleEngine.popen_uci("/path/to/stockfish")

# define the board and initialize the game
board = chess.Board()

# loop over the game until it's over
while not board.is_game_over():
    # if it's the bot's turn, generate a move
    if board.turn == chess.WHITE:
        # use the Stockfish engine to generate the best move
        result = engine.play(board, chess.engine.Limit(time=2.0))
        move = result.move

        # make the move on the board
        board.push(move)

    # if it's the player's turn, ask for input and make the move
    else:
        move = input("Enter your move: ")
        board.push_san(move)

    # print the board after the move
    print(board)

# print the result of the game
print("Game over. Result: ", board.result())

# close the Stockfish engine
engine.quit()
