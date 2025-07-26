# 🐍 Snake Game – Classic Snake in Python with Sound Effects 🎮🔊

Welcome to **Snake Game**, a modern twist on the nostalgic arcade classic — built entirely with **Python + Tkinter**, and spiced up with cool **MP3 sound effects** using `playsound3`! 🍎💥

![Snake Game Banner](https://github.com/Golu-Guptha/snake_game_tkinter/blob/main/game_over.png)

---

## 🚀 Features

- 🎨 **Clean GUI** using Python's built-in `Tkinter`
- 🔊 **Realistic sound effects** on eating food and game over
- 🔁 Press **Enter** to restart anytime
- 🎯 Simple keyboard controls: Arrow keys to move
- 🧠 Smart food spawning (never on the snake's body!)
- ⚡ Light & fast — no external game engine required

---

## 🎮 How to Play

> Use your arrow keys to move the snake and eat red food (🍎) to grow longer.  
> Avoid hitting the walls or yourself.  
> When you die, press **Enter** to play again!

| Key | Action |
|-----|--------|
| ⬆️  | Move Up |
| ⬇️  | Move Down |
| ⬅️  | Move Left |
| ➡️  | Move Right |
| ↵ (Enter) | Restart Game |

---

## 🛠️ Setup Instructions

1. **Clone this repository:**

   ```bash
   git clone https://github.com/your-username/snake-game-tkinter.git
   cd snake-game-tkinter
   ```

2. **Install Dependencies:**

   ```bash
   pip install playsound3
   ```

3. **Add MP3 Sound Files:**

   Make sure the `./assets/` folder contains:

   - `eat.mp3` — sound when snake eats food  
   - `gameover.mp3` — sound when game ends

   > 📝 Rename or replace with your own audio files if you'd like to customize the sounds!

4. **Run the Game:**

   ```bash
   python snake_game.py
   ```

---

## 🖼️ Screenshots

| Gameplay | Game Over |
|----------|-----------|
| ![play](https://github.com/Golu-Guptha/snake_game_tkinter/blob/main/play.png) | ![gameover](https://github.com/Golu-Guptha/snake_game_tkinter/blob/main/game_over.png) |

---

## 📁 Project Structure

```bash
snake-game-tkinter/
│
├── assets/
│   ├── eat.mp3
│   └── gameover.mp3
│
├── snake_game.py     # Main game script
└── README.md
```

---

## ✨ What Makes It Cool?

- Uses `playsound3` for **non-blocking audio playback** 🎧
- **Smart respawning** of food – never overlaps the snake
- Clean and minimal **code structure** for easy learning and modification
- Easily expandable with themes, difficulty levels, or a high score system 🔥

---

## 🧠 Learning Outcome

This project is ideal for:
- Tkinter GUI practice
- Canvas-based 2D graphics
- Event handling and game loops
- Thread-safe sound integration
- Building restartable game logic in Python

---

## 🤝 Contributing

Want to add features like power-ups, walls, or high scores? Fork the repo and submit a pull request!  
Help us grow this classic game with modern features! 🙌

---

## 📜 License

This project is licensed under the MIT License.  
Feel free to use, modify, or distribute with attribution. 👍

---

## 🐍 Made With Python & Passion ❤️  
> Because some classics never go out of style.
