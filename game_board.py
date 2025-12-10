
import math

# إعدادات اللعبة
ROWS = 6
COLS = 7
EMPTY = 0
PLAYER = 1
AI = 2
COLORS = {EMPTY: "white", PLAYER: "red", AI: "blue"} 

class Connect4:
    def __init__(self):
        self.rows = ROWS
        self.cols = COLS
        self.board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

    def copy(self):
        new = Connect4()
        new.board = [row[:] for row in self.board]
        return new

    def valid_moves(self):
        # الأعمدة اللي لسه فيها مكان
        return [c for c in range(self.cols) if self.board[0][c] == EMPTY]

    def make_move(self, col, piece):
        # بنحط القطعة في العمود، لو اتعملت ترجع True
        for r in reversed(range(self.rows)):
            if self.board[r][col] == EMPTY:
                self.board[r][col] = piece
                return True
        return False 

    def is_full(self):
        # اللوحة اتملت ولا لسه؟
        return all(self.board[0][c] != EMPTY for c in range(self.cols))

    def terminal(self):
        return self.is_full()

    def count_fours(self, piece):
        # بنعد كام 4 متتالية عند اللاعب ده (أفقي - رأسي - قطري)
        count = 0
        b = self.board

        # أفقي
        for r in range(self.rows):
            for c in range(self.cols - 3):
                if all(b[r][c+i] == piece for i in range(4)): count += 1

        # رأسي
        for c in range(self.cols):
            for r in range(self.rows - 3):
                if all(b[r+i][c] == piece for i in range(4)): count += 1

        # قطر موجب
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                if all(b[r+i][c+i] == piece for i in range(4)): count += 1

        # قطر سالب
        for r in range(3, self.rows):
            for c in range(self.cols - 3):
                if all(b[r-i][c+i] == piece for i in range(4)): count += 1

        return count


def heuristic(board: Connect4, piece=AI):
    score = 0
    opp_piece = 3 - piece  # أحسن وأسرع طريقة: اللي مش أنا هو الخصم
    b = board.board

    center_col = COLS // 2
    score += sum(1 for r in range(ROWS) if b[r][center_col] == piece) * 6

    def eval_window(w):
        # بنقيّم كل 4 خلايا جنب بعض
        s = 0
        if w.count(piece) == 4:      s += 10000   # فوز فوري
        elif w.count(piece) == 3 and w.count(EMPTY) == 1: s += 100
        elif w.count(piece) == 2 and w.count(EMPTY) == 2: s += 10
        if w.count(opp_piece) == 3 and w.count(EMPTY) == 1: s -= 80  
        return s

    # أفقي
    for r in range(ROWS):
        for c in range(COLS-3):
            score += eval_window(b[r][c:c+4])

    # رأسي
    for c in range(COLS):
        for r in range(ROWS-3):
            score += eval_window([b[r+i][c] for i in range(4)])

    # الاقطار
    for r in range(ROWS-3):
        for c in range(COLS-3):
            score += eval_window([b[r+i][c+i] for i in range(4)])
    for r in range(3, ROWS):
        for c in range(COLS-3):
            score += eval_window([b[r-i][c+i] for i in range(4)])

    return score