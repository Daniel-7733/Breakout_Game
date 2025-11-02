# Breakout (Python Turtle)

A simple **Breakout**-style game built with Python’s standard `turtle` graphics module. This project is a learning sandbox to practice object‑oriented design, basic rendering, and input handling.


---

## ✨ Features (current state)
- Window setup with custom background color
- **Paddle** (player racket) you can move with the **Left / Right** arrow keys
- A **ball** that moves continuously on a timer
- A grid of **bricks** drawn at the top of the screen

---

## 🗂️ Project structure

```
.
├── main.py          # Entry point: starts the game
├── game.py          # Game container: creates screen and game objects
├── player.py        # Player paddle (racket) and movement
├── ball.py          # Ball sprite and constant movement loop
├── brick.py         # Brick drawing & layered grid
└── .gitignore
```

---

## ▶️ How to run

**Requirements**
- Python 3.10+ (turtle is included with the Python standard library)
- Works on Windows/macOS/Linux (ensure you have a GUI environment)

**Run the game**
```bash
python main.py
```

**Controls**
- **Left Arrow**: move paddle left
- **Right Arrow**: move paddle right

---

## 🧱 What’s implemented in code (high level)

- `main.py` starts the program and creates a `Game` instance.
- `game.py` sets up the window (title, background), creates the **Player**, **Ball**, and **Brick** objects, and starts the main loop.
- `player.py` draws a rectangle‑like paddle using the square shape (stretched) and binds **Left/Right** keys for movement.
- `ball.py` creates a circular turtle and uses `ontimer` to move the ball every few milliseconds (simple constant motion).
- `brick.py` draws filled rectangles in a layered grid using simple turtle drawing commands.

---

## 🛣️ Roadmap / TODO

- [ ] Ball–wall collisions (bounce on window edges)
- [ ] Ball–paddle collision (reflect with angle based on hit position)
- [ ] Ball–brick collisions (remove bricks, increase score)
- [ ] Score, lives, and UI text
- [ ] Game over / win screen
- [ ] Sound effects (optional)
- [ ] Level layout variations
- [ ] Code refactors (separate constants, collision helper functions, etc.)

---
👨‍💻 Created as a practice project to learn Python and GitHub. Built with by Daniel