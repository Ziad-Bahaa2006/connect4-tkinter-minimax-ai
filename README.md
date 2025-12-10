# 🎮 Connect 4 — AI Powered Game (Minimax + Alpha-Beta Pruning)

> An advanced implementation of **Connect 4** using Python, featuring a smart AI opponent, modern GUI, and a strategic heuristic system.  
> Built collaboratively as a team project with clean code, modular structure, and professional documentation.

---

## 🔗 GitHub Repository  
👉 **Repo Link:**  
`https://github.com/Ziad-Bahaa2006/connect4-tkinter-minimax-ai`

---

## 👥 Team Members

| Name | ID | Role |
|------|------|------|
| **Ziad Bahaa Elsayed Taha** | 2405720 | AI Logic, GUI Integration, Game Mechanics |
| **Mohammed Islam Ibrahim** | 2405736 | GUI Design, User Experience |
| **Mohammed Elmesarea** | 2405727 | Board Logic, Optimization |
---

## 🧠 Project Overview

This project delivers a polished, interactive version of **Connect 4**, enhanced with:

- A fully functional **Tkinter GUI**
- Circular tokens for an authentic Connect 4 look
- Four difficulty levels powered by **Minimax + Alpha-Beta Pruning**
- A robust **heuristic evaluation function**
- A win condition based on **"Most 4-in-a-Row Chains Wins"** instead of the standard first-4

The project is modular, clean, and follows software engineering best practices.

---

## 🚀 Features

### 🎨 Elegant GUI (Tkinter + Canvas)
- Smooth circular pieces  
- Clean color palette  
- Responsive layout  
- Difficulty selector screen  

### 🧠 Smart AI Opponent
Built using:

- **Minimax Algorithm**  
- **Alpha-Beta Pruning**  
- **Move Tree Exploration**  
- **State Evaluation Heuristic**

The AI evaluates future board states and picks the best possible move depending on the chosen difficulty.

### 🎚️ Difficulty Levels

| Mode | Depth | Description |
|------|--------|-------------|
| Easy | 3 | Simple, fast decisions |
| Medium | 4 | Balanced gameplay |
| Hard | 5 | Strong AI |
| Impossible | 6 | Very hard to beat |

---

## 🧩 Project Structure

```
.
├── game_board.py        # Board logic, valid moves, heuristic scoring
├── ai_engine.py         # Minimax + Alpha-Beta pruning + tree nodes
├── main.py              # Tkinter GUI and game flow control
```

Each file is independent and follows a clean, maintainable architecture.

---

## 🧠 AI Logic — How It Works

### 1️⃣ **Minimax Algorithm**
Simulates all future moves for both players, assuming perfect play.

### 2️⃣ **Alpha-Beta Pruning**
Optimizes Minimax by skipping branches that don’t affect the final decision.  
This dramatically speeds up higher difficulty levels.

### 3️⃣ **Heuristic Evaluation Function**
The AI scores each board using rules such as:

- Central column priority  
- 2-in-a-row, 3-in-a-row patterns  
- Penalties for opponent threats  
- Guaranteed wins (4 in a row = +10000)

This makes the AI smart, aggressive, and unpredictable.

---

## 🎯 Game Logic: “Most 4-Chains Wins”

Unlike the classic version:
- The game **doesn’t end when someone makes the first 4**.
- Instead, when the board is full:
  - The player with **more 4-in-a-row chains** wins.
  - This encourages strategy, blocking, and long-term planning.

---

## ▶️ How to Run

### 1️⃣ Install Python  
Make sure Python 3.8+ is installed.

### 2️⃣ Run the game  
```
python main.py
```

No external libraries needed — only Tkinter (pre-installed with Python).

---

## 🔮 Future Enhancements

- Animated falling discs  
- Sound effects for moves and winning  
- Player vs Player mode  
- Dark mode GUI  
- Saving/loading game states  

---

## 📄 License  
This project is for educational and academic use.  
Feel free to modify and extend it.

---

## ⭐ Special Notes  
This project showcases:

- Professional code structure  
- Real AI search techniques  
- GUI programming  
- Team collaboration  
- Clean documentation  
