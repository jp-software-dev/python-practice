# Python Engineering & Security Workspace 🐍

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Data Analysis](https://img.shields.io/badge/Data_Analysis-Algorithms_&_AI-orange?style=for-the-badge)
![Red Team](https://img.shields.io/badge/Red_Team-Offensive_Ops-darkred?style=for-the-badge&logo=kalilinux&logoColor=white)
![Blue Team](https://img.shields.io/badge/Blue_Team-Defensive_Ops-blue?style=for-the-badge&logo=fortinet&logoColor=white)

This repository is a comprehensive engineering workspace dedicated to advanced Python programming, data analysis, and full-spectrum cybersecurity operations. It is intentionally structured to showcase a progression from foundational logic challenges to complex neural networks and applied security tooling.

## 🗂️ Repository Architecture & Scope

Rather than a single monolithic application, this workspace contains modular, standalone projects categorized by their technical discipline and complexity level:

* **🛡️ Cybersecurity (Red & Blue Team):** Applied security tooling covering both **Red Team** operations (offensive scripting, footprinting, concurrent network scanners) and **Blue Team** operations (defensive auditing, secure protocols, local environment hardening).
* **📊 Data Analysis & AI (Análisis de Datos):** Advanced data processing implementations featuring dedicated modules for complex **Algorithms** and machine learning **Neural Networks**.
* **🧠 Progressive Engineering (Ejercicios & Retos):** A strictly organized learning and logic path containing scripts divided by complexity (`Principiante`, `Intermedio`, `Avanzado`) alongside a complete `100 Days of Code` challenge focusing on core Python mechanics, memory management, and data structures.
* **🛠️ Practical Utilities (QR Generators):** Functional automation scripts for generating and managing QR codes across various formats (Links, Images, and Text).
* **💾 Database Operations:** Local persistence implementations handling relational CRUD operations utilizing `SQLite3` (e.g., inventory systems and URL tracking).

## 💻 Tech Stack & Libraries

* **Core Language:** Python 3.x (OOP, Multithreading)
* **Data & AI:** `TensorFlow`, `NumPy`, `Pandas`, `Matplotlib`
* **Security & Networking:** `cryptography`, `socket`, `threading`
* **Data Handling:** `sqlite3`, `requests`, `bs4` (BeautifulSoup)
* **System Automation:** `os`, `sys`, custom internal logging

## 🚀 Getting Started

To explore, review, or run these scripts locally within a Windows environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/jp-software-dev/python-practice.git
   ```

2. Navigate into the project directory:
   ```bash
   cd python-practice
   ```

3. Install the third-party libraries used by some scripts (the rest only need the standard library):
   ```bash
   pip install requests beautifulsoup4 "qrcode[pil]" pillow pygame psutil colorama
   ```

4. Run any script (use quotes, many paths contain spaces):
   ```bash
   python "Ejercicios Intermedio/juego_snake.py"
   ```

> For the socket chat, start `servidor.py` first and then one or more `cliente.py` in separate terminals.

## 📚 How to Learn With This Repository

This repo is my own learning path, shared so anyone can follow it. If you are starting with Python, you can use it as a step-by-step guide: every script is short, standalone and focused on one idea, so you can open it, read it, run it and change it without setting anything else up.

> Comments, variable names and console messages are mostly in **Spanish**.

### 🧭 Suggested path

Follow the folders in this order. Each stage builds on the previous one.

| Step | Folder | What you will learn |
| --- | --- | --- |
| 1 | `Curso Python/` | The basics: variables, input, type conversion, strings, indexing, lists, tuples, sets, dictionaries, `if`, `for` / `while` loops and `break` / `continue`. |
| 2 | `Reto de 100 Dias/` | Daily practice. Short exercises (`P1.py`, `P2.py`…) that start with simple math and grow into functions, `lambda`, `map` and classes. Do one per day. |
| 3 | `Ejercicios Principiante/` | Your first complete programs: games (hangman, rock-paper-scissors, guessing), a tip calculator, unit converter, To-Do list, Pomodoro timer, file organizer and small apps that call public APIs. |
| 4 | `Ejercicios Intermedio/` | Real-world tools: SQLite databases (URL shortener, inventory), web scraping, a crypto price viewer, an image editor with Pillow, a Snake game with Pygame, a notes app with password hashing and a voting system. |
| 5 | `Ejercicios Intermedio/Ejercicios con Sockets/` | Networking from zero: TCP and UDP sockets, DNS lookups, IP conversion and XML-RPC. Files ending in `.1` are the client for the server with the same number (run `3.py`, then `3.1.py`). |
| 6 | `Ejercicios Intermedio/Aplicación de Chat con Sockets/` | Puts the networking together: a multi-client chat using sockets and threads. |
| 7 | `Ejercicios Avanzado/` | Multithreading with a port scanner and a GUI calendar with Tkinter. |
| 8 | `Qr-Enlaces/`, `Qr-Imagenes/`, `Qr-Texto/` | Small automation utilities that generate QR codes. |

### 💡 Tips to get the most out of it

1. **Read before you run.** Try to predict what the script will print, then run it and compare.
2. **Change one thing at a time.** Edit a value, a condition or a loop and see what happens. Breaking the code on purpose is one of the fastest ways to learn.
3. **Rewrite it from scratch.** After understanding a script, close it and write your own version without looking.
4. **Add a feature.** Every project can grow: add a score to a game, a new table to a database app, or a menu option to a tool.
5. **Keep your own notes.** Write down what each script taught you; it becomes your personal cheat sheet.

### ⚠️ About the security scripts

The networking and security scripts (like the port scanner) are for learning how systems work. Only run them on your own computer or on networks and devices you have explicit permission to test.

### 🤝 Feedback

Found a bug, have an idea for a new exercise or a better way to solve one? Open an issue or a pull request. Suggestions are welcome.
