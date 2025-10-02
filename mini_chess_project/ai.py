import chess
import math
import random

PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

def evaluate_board(board: chess.Board) -> int:
    """Simple evaluation: material balance (positive = white advantage)."""
    if board.is_checkmate():
        # if white to move and checkmate -> white lost
        return -99999 if board.turn else 99999
    if board.is_stalemate():
        return 0

    value = 0
    for piece_type in PIECE_VALUES:
        value += len(board.pieces(piece_type, chess.WHITE)) * PIECE_VALUES[piece_type]
        value -= len(board.pieces(piece_type, chess.BLACK)) * PIECE_VALUES[piece_type]
    # small bonus for mobility
    value += 0.1 * (len(list(board.legal_moves)) if board.turn else -len(list(board.legal_moves)))
    return int(value)

def minimax(board: chess.Board, depth: int, alpha: int, beta: int, maximizing: bool):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    best_move = None
    if maximizing:
        max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            eval_score, _ = minimax(board, depth-1, alpha, beta, False)
            board.pop()
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in board.legal_moves:
            board.push(move)
            eval_score, _ = minimax(board, depth-1, alpha, beta, True)
            board.pop()
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, best_move

def select_move(board: chess.Board, depth: int = 3):
    """Select move for the side to move using minimax + alpha-beta."""
    maximizing = board.turn  # True if white to move
    _, move = minimax(board, depth, -float('inf'), float('inf'), maximizing)
    # if no move found (shouldn't happen), pick random legal move
    if move is None:
        moves = list(board.legal_moves)
        return random.choice(moves) if moves else None
    return move
