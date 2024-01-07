import colorama
import tttlib

board = tttlib.Board()

# The minimax algorithm I have implemented takes 4 arguments:
# the board, a boolean representing whether the current player is the maximizing player,
# and alpha and beta values for alpha-beta pruning.
# The algorithm returns the score of the board,
# which is 1 if the maximizing player wins, -1 if the minimizing player wins, and 0 if the game is a draw.

# There is no depth limit to this minimax algorithm since tic-tac-toe can only ever go for 9 moves
# (and the game tree is only 9 levels deep), so most computers can handle it just fine.
def minimax(board, isMax, alpha, beta):
    # Check for a win or draw at the end of the game tree.
    score = board.check_win()
    # Exit the game tree if a terminal state has been reached.
    if score is not None:
        return score

    # If the current player is the maximizing player (in this case, X),
    if isMax:
        # initialize the best value to -1000 (the worst possible score for the maximizing player).
        best = -1000
        # For each possible move,
        for move in board.moves:
            # make the move,
            board.move(move)
            # and recursively call minimax on the resulting board state.
            # The player in the new game state is now the minimizing player, so isMax is set to False.
            # The alpha and beta values are also passed down.
            # The best value is set to the maximum of the current best value and the value returned by the recursive call,
            # so we don't lose track of the best move.
            best = max(best, minimax(board, False, alpha, beta))
            # Unmake the move so the board is back to normal.
            board.unmove(move)
            # If the move we have found is so good that the opponent would reasonably never let us make it,
            # we can stop searching the game tree early, returning the best value we have found so far.
            # Beta is the best value that the minimizing player can guarantee at this point in the game tree.
            if best >= beta:
                break
            # Otherwise, we update alpha to be the maximum of the current alpha and the best value we have found so far.
            # Alpha is the best value that the maximizing player can guarantee at this point in the game tree.
            alpha = max(alpha, best)

        return best
    # If the current player is the minimizing player (in this case, O),
    else:
        # initialize the best value to 1000 (the worst possible score for the minimizing player).
        best = 1000
        # For each possible move,
        for move in board.moves:
            # make the move,
            board.move(move)
            # and recursively call minimax on the resulting board state.
            # The player in the new game state is now the maximizing player, so isMax is set to True.
            # The alpha and beta values are also passed down.
            # The best value is set to the minimum of the current best value and the value returned by the recursive call,
            # so we don't lose track of the best move.
            best = min(best, minimax(board, True, alpha, beta))
            # Unmake the move so the board is back to normal.
            board.unmove(move)
            # If the move we have found is so good that the opponent would reasonably never let us make it,
            # we can stop searching the game tree early, returning the best value we have found so far.
            # Alpha is the best value that the maximizing player can guarantee at this point in the game tree.
            if best <= alpha:
                break
            # Otherwise, we update beta to be the minimum of the current beta and the best value we have found so far.
            # Beta is the best value that the minimizing player can guarantee at this point in the game tree.
            beta = min(beta, best)

        return best

def engine_move():
    # We set the best value to be the worst value for the player whose turn it is.
    bestVal = -1000 if board.turn == 1 else 1000
    # We set the best move to be an invalid move.
    bestMove = -1
    # For each possible move in the current board state
    for move in board.moves:
        # make the move,
        board.move(move)
        # and call minimax on the resulting board state.
        # The player in the new game state is now the minimizing player if the current player is the maximizing player,
        # and vice versa.
        # Alpha and beta are initialized to -1000 and 1000 respectively,
        # since these are the worst possible values for the maximizing and minimizing players.
        # These values will be updated as the game tree is searched.
        # But since any searched moves do not affect the current board state,
        # we can just toss out the previous alpha and beta values.
        moveVal = minimax(board, board.turn == 1, -1000, 1000)
        # Unmake the move so the board is back to normal.
        board.unmove(move)
        # If the move we have found is better than the best move we have found so far,
        if (board.turn == 1 and moveVal > bestVal) or (board.turn == -1 and moveVal < bestVal):
            # update the best move and best value.
            bestMove = move
            bestVal = moveVal
    return bestMove


if __name__ == "__main__":
    player = input("Would you like to play as "+colorama.Fore.LIGHTGREEN_EX+"X"+colorama.Fore.RESET+" or "+colorama.Fore.LIGHTRED_EX+"O"+colorama.Fore.RESET+"?")
    player = 1 if (player.upper() == "X") else -1 if (player.upper() == "O") else 0
    if player == 0:
        raise(Exception("Invalid player."))
    print(colorama.Fore.LIGHTGREEN_EX+"X TURN"+colorama.Fore.RESET)
    board.display()
    if player == -1:
        board.move(engine_move())
        print(colorama.Fore.LIGHTRED_EX+"O TURN"+colorama.Fore.RESET)
        board.display()

    while True:
        move = int(input("Enter a move: "))
        if move not in board.moves:
            print("Invalid move.")
            continue
        board.move(move)
        print(colorama.Fore.LIGHTGREEN_EX+"X TURN"+colorama.Fore.RESET if board.turn == 1 else colorama.Fore.LIGHTRED_EX+"O TURN"+colorama.Fore.RESET)
        board.display()
        if board.check_win() is not None:
            print(colorama.Fore.LIGHTGREEN_EX+"X WINS"+colorama.Fore.RESET if board.check_win() == 1 else colorama.Fore.LIGHTRED_EX+"O WINS"+colorama.Fore.RESET if board.check_win() == -1 else colorama.Fore.LIGHTBLUE_EX+"DRAW"+colorama.Fore.RESET)
            break
        board.move(engine_move())
        print(colorama.Fore.LIGHTGREEN_EX+"X TURN"+colorama.Fore.RESET if board.turn == 1 else colorama.Fore.LIGHTRED_EX+"O TURN"+colorama.Fore.RESET)
        board.display()
        if board.check_win() is not None:
            print(colorama.Fore.LIGHTGREEN_EX+"X WINS"+colorama.Fore.RESET if board.check_win() == 1 else colorama.Fore.LIGHTRED_EX+"O WINS"+colorama.Fore.RESET if board.check_win() == -1 else colorama.Fore.LIGHTBLUE_EX+"DRAW"+colorama.Fore.RESET)
            break