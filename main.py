
import tkinter as tk
from tkinter import messagebox
from game_board import Connect4, PLAYER, AI, COLORS
from ai_engine import get_ai_move

class Connect4Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connect 4 - Most 4-in-a-rows Wins!")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f4f4")
        self.show_difficulty_selection()

    def show_difficulty_selection(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Select AI Difficulty", font=("Arial", 22, "bold"), bg="#f4f4f4").pack(pady=40)

        options = [
            ("Easy (Depth 3)", 3),
            ("Medium (Depth 4)", 4),
            ("Hard (Depth 5)", 5),
            ("Impossible (Depth 6)", 6)
        ]

        for text, depth in options:
            btn = tk.Button(self.root, text=text, font=("Arial", 16), width=28, height=2,
                            bg="#2c3e50", fg="white", command=lambda d=depth: self.start_game(d))
            btn.pack(pady=12)

    def start_game(self, depth):
        self.depth = depth
        self.game = Connect4()
        self.turn = PLAYER

        for widget in self.root.winfo_children():
            widget.destroy()

        # Title
        tk.Label(self.root, text="Connect 4", font=("Arial", 28, "bold"), bg="#f4f4f4").grid(row=0, column=0, columnspan=7, pady=10)

        # Column buttons
        self.buttons = []
        for c in range(7):
            btn = tk.Button(self.root, text=str(c+1), font=("Arial", 16, "bold"),
                            width=8, height=2, bg="#2c3e50", fg="white",
                            command=lambda col=c: self.player_move(col))
            btn.grid(row=1, column=c, padx=5, pady=10)
            self.buttons.append(btn)

        # Board cells
        self.cells = []
        for r in range(6):
            row_cells = []
            for c in range(7):
                cell = tk.Canvas(self.root, width=60, height=60, bg="#f4f4f4", highlightthickness=0)
                cell.grid(row=r+2, column=c, padx=5, pady=5)
                circle = cell.create_oval(5, 5, 55, 55, fill="white", outline="#444", width=4)
                row_cells.append((cell, circle))
            self.cells.append(row_cells)


        # Bottom controls
        bottom = tk.Frame(self.root, bg="#f4f4f4")
        bottom.grid(row=9, column=0, columnspan=7, pady=20)

        self.status_label = tk.Label(bottom, text="Your turn (Red)", font=("Arial", 16), fg="red", bg="#f4f4f4")
        self.status_label.pack(side=tk.LEFT, padx=30)

        tk.Label(bottom, text=f"Difficulty: Depth {depth}", font=("Arial", 12), bg="#f4f4f4").pack(side=tk.RIGHT, padx=20)

        tk.Button(bottom, text="Restart Game", font=("Arial", 12, "bold"),
                  bg="#e74c3c", fg="white", width=15, command=self.restart).pack(side=tk.RIGHT, padx=10)

        self.update_board()

    def update_board(self):
        for r in range(6):
            for c in range(7):
                cell, circle = self.cells[r][c]
                cell.itemconfig(circle, fill=COLORS[self.game.board[r][c]])

    def player_move(self, col):
        if self.turn != PLAYER or col not in self.game.valid_moves():
            return

        self.game.make_move(col, PLAYER)
        self.update_board()

        if self.game.terminal():
            self.end_game()
            return

        self.turn = AI
        self.status_label.config(text="AI is thinking...", fg="blue")
        self.root.after(300, self.ai_move)

    def ai_move(self):
        col, stats = get_ai_move(self.game, self.depth, print_debug=True)

        if col is not None:
            self.game.make_move(col, AI)
            self.update_board()

        if self.game.terminal():
            self.end_game()
            return

        self.turn = PLAYER
        self.status_label.config(text="Your turn (Red)", fg="red")

    def end_game(self):
        for btn in self.buttons:
            btn.config(state="disabled")

        p = self.game.count_fours(PLAYER)
        a = self.game.count_fours(AI)

        if p > a:
            msg = f"You Win!\nRed: {p} fours | Blue: {a}"
            color = "red"
        elif a > p:
            msg = f"AI Wins!\nRed: {p} | Blue: {a} fours"
            color = "blue"
        else:
            msg = f"Draw!\nBoth have {p} fours"
            color = "purple"

        self.status_label.config(text=msg, fg=color, font=("Arial", 18, "bold"))

    def restart(self):
        if messagebox.askyesno("Restart", "Choose a new difficulty?"):
            self.show_difficulty_selection()
        else:
            self.start_game(self.depth)

if __name__ == "__main__":
    game = Connect4Game()
    game.root.mainloop()
