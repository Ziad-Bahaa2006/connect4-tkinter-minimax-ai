import tkinter as tk
from Assignment_2 import connect4, player, AI, heuristic
from connect_4_minimax_task_2 import get_ai_move

class Connect4GUI:
    def __init__(self):
        self.game = connect4()
        self.turn = player

        self.root = tk.Tk()
        self.root.title("Connect 4")

        self.buttons = []
        for c in range(self.game.cols):
            b = tk.Button(self.root, text=str(c+1), width=6, height=2,
                          command=lambda col=c: self.player_move(col))
            b.grid(row=0, column=c)
            self.buttons.append(b)

        self.labels = [[None for _ in range(self.game.cols)] for _ in range(self.game.rows)]
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                l = tk.Label(self.root, width=6, height=2, relief="ridge", bg="white")
                l.grid(row=r+1, column=c)
                self.labels[r][c] = l

        self.root.mainloop()

    def update_board(self):
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                v = self.game.board[r][c]
                if v == player:
                    self.labels[r][c].config(bg="red")
                elif v == AI:
                    self.labels[r][c].config(bg="blue")
                else:
                    self.labels[r][c].config(bg="white")

    def player_move(self, col):
        if self.turn != player:
            return
        if not self.game.Make_move(col, player):
            return
        self.update_board()
        if self.game.Check_winner(player):
            self.end("Player Wins")
            return
        if self.game.is_full():
            self.end("Draw")
            return
        self.turn = AI
        self.root.after(200, self.ai_move)

    def ai_move(self):
        adapter = Adapter(self.game)
        col = get_ai_move(self.game.copy(), 3, adapter)
        self.game.Make_move(col, AI)
        self.update_board()
        if self.game.Check_winner(AI):
            self.end("AI Wins")
            return
        if self.game.is_full():
            self.end("Draw")
            return
        self.turn = player

    def end(self, msg):
        for b in self.buttons:
            b.config(state="disabled")
        w = tk.Label(self.root, text=msg, font=("Arial", 16))
        w.grid(row=self.game.rows + 2, column=0, columnspan=self.game.cols)

class Adapter:
    def __init__(self, game):
        self.game = game
        self.AI = AI
        self.PLAYER = player

    def get_valid_locations(self, board):
        return board.Valid_moves()

    def make_move(self, board, col, piece):
        b = board.copy()
        b.Make_move(col, piece)
        return b

    def is_terminal(self, board):
        return board.terminal_state()

    def score_position(self, board):
        return heuristic(board, AI)

if __name__ == "__main__":
    Connect4GUI()
