"""
Mini Chess CLI with simple Minimax AI (requires python-chess).
Instructions in README.md (Bangla).
"""
import chess
from ai import select_move
import sys

def print_board(board):
    # Print board with ranks 8->1
    print(board)

def player_move(board):
    while True:
        move_input = input("Your move (e.g. e2e4 or 'quit'): ").strip()
        if move_input.lower() in ("quit","exit"):
            sys.exit(0)
        try:
            move = chess.Move.from_uci(move_input)
            if move in board.legal_moves:
                return move
            else:
                print("Illegal move. Try again.")
        except Exception as e:
            print("Invalid format. Use UCI like e2e4 or g1f3.")

def main():
    print("Mini Chess CLI (you play as White).")
    print("To play, enter moves in UCI format, e.g. e2e4, g1f3, e7e8q (promotion).")
    print("AI uses a simple minimax (depth-limited).")
    depth = 3
    try:
        d = input(f"Choose AI depth (recommended 2-4) [default {depth}]: ").strip()
        if d:
            depth = int(d)
    except:
        pass

    board = chess.Board()
    while True:
        print_board(board)
        if board.turn:  # White to move (human)
            move = player_move(board)
            board.push(move)
        else:
            print("AI thinking...")
            move = select_move(board, depth)
            if move is None:
                print("No legal moves for AI.")
                break
            print("AI plays:", move.uci())
            board.push(move)

        if board.is_checkmate():
            print_board(board)
            if board.turn:
                print("Checkmate! Black wins.")
            else:
                print("Checkmate! White wins.")
            break
        if board.is_stalemate():
            print("Stalemate.")
            break
        if board.is_insufficient_material():
            print("Draw (insufficient material).")
            break
        if board.can_claim_threefold_repetition():
            print("Threefold repetition possible (draw can be claimed).")
            break

if __name__ == "__main__":
    main()
