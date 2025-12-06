# Connect 4 Game (Tkinter + Minimax AI)

A fully implemented **Connect 4** game built with **Python**, featuring a clean **Tkinter GUI** and a competitive **Minimax AI** player. This project demonstrates game development, search algorithms, GUI programming, and heuristic-driven decision‑making.

---

## 🚀 Features

* **Interactive GUI** built with Tkinter.
* **Player vs AI** gameplay.
* AI powered by **Minimax algorithm (depth = 3)**.
* Custom **heuristic evaluation** for smart decision‑making.
* Automatic win/draw detection.
* Fully modular: game logic, AI logic, and GUI are separated for readability.

---

## 🧠 AI Logic (Minimax + Heuristic)

The AI evaluates possible moves using:

* **Minimax search tree** up to depth 3.
* Custom **score_position()** heuristic.
* Automatic board copying and simulation.

This allows the AI to:

* Predict and block player winning moves.
* Maximize its own winning opportunities.
* Play strategically even with low computational cost.

---

## 📁 Project Structure

```
project-folder/
│
├── main_gui.py                   # Tkinter GUI 
├── Assignment_2.py               # Core game logic + heuristic function
├── connect_4_minimax_task_2.py   # Minimax + get_ai_move() implementation
│
```

---

## 🛠️ Installation & Running

### 1) Ensure Python 3 is installed

```
python --version
```

### 2) Run the game

```
python main_gui.py
```

A window will launch and gameplay will begin immediately.

---

## 👥 Team Members

* **Mohamed Islam Ibrahim - 2405736** – GUI & overall integration
* **Mohamed Elmesarea - 2405727** – Game logic & heuristic design
* **Ziad Bahaa Elsayed** – Minimax algorithm implementation
---

## 🧩 Technologies Used

* **Python 3**
* **Tkinter** (GUI)
* **Minimax Algorithm**
* **Heuristic Evaluation for AI**

---

## 🤝 Contributing

Contributions, improvements, and enhancements are welcome.
Feel free to open a Pull Request.
