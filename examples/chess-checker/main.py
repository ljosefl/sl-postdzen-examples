from chess import Board
from chess import Move

def check_chess_move(move_str):
    board = Board()
    try:
        move = Move.from_uci(move_str)
        if board.is_legal(move):
            print(f"Ход {move} корректен")
        else:
            print(f"Ход {move} неверен")
    except ValueError:
        print(f"Неверный ход: {move_str}")

# Пример использования
check_chess_move("e4e5")