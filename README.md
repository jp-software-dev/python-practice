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

## 🗺️ Learning Roadmap

This repository grows step by step. Each project is added here as it is completed.

✅ Completed · ▶️ In progress · ⏳ Planned

### 🟢 Beginner Level — Completed

| # | Project | File |
| --- | --- | --- |
| 1 | ✅ Tip calculator | [`Calculadora de propinas.py`](<Ejercicios Principiante/Calculadora de propinas.py>) |
| 2 | ✅ Rock, paper, scissors | [`Juego Clasico.py`](<Ejercicios Principiante/Juego Clasico.py>) |
| 3 | ✅ Digital clock with GUI | [`Reloj Digital.py`](<Ejercicios Principiante/Reloj Digital.py>) |
| 4 | ✅ Simple link shortener | [`Acortador de enlaces.py`](<Ejercicios Principiante/Acortador de enlaces.py>) |
| 5 | ✅ File organizer by extension | [`Organizador de archivos.py`](<Ejercicios Principiante/Organizador de archivos.py>) |
| 6 | ✅ Word counter | [`Contador de palabras.py`](<Ejercicios Principiante/Contador de palabras.py>) |
| 7 | ✅ Unit converter (Celsius ↔ Fahrenheit) | [`Convertidor de unidades.py`](<Ejercicios Principiante/Convertidor de unidades.py>) |
| 8 | ✅ To-Do list | [`Lista de tareas pendientes.py`](<Ejercicios Principiante/Lista de tareas pendientes.py>) |
| 9 | ✅ Dice roll simulator | [`Lanzamiento de dados..py`](<Ejercicios Principiante/Lanzamiento de dados..py>) |
| 10 | ✅ Countdown timer (Pomodoro) | [`Reloj de cuenta regresiva.py`](<Ejercicios Principiante/Reloj de cuenta regresiva.py>) |
| 11 | ✅ Dictionary definition finder | [`Buscador de definiciones diccionario.py`](<Ejercicios Principiante/Buscador de definiciones diccionario.py>) |
| 12 | ✅ Palindrome checker | [`Verificador de palíndromo.py`](<Ejercicios Principiante/Verificador de palíndromo.py>) |
| 13 | ✅ Current weather notifier | [`Notificador de clima actual.py`](<Ejercicios Principiante/Notificador de clima actual.py>) |
| 14 | ✅ Hangman game | [`Juego del ahorcado.py`](<Ejercicios Principiante/Juego del ahorcado.py>) |

### 🟡 Intermediate Level — In Progress

| # | Project | File |
| --- | --- | --- |
| 15 | ✅ Web data extractor (price scraper) | [`web_scraper.py`](<Ejercicios Intermedio/web_scraper.py>) |
| 16 | ✅ URL shortener with SQLite database | [`acortador_sqlite.py`](<Ejercicios Intermedio/acortador_sqlite.py>) |
| 17 | ✅ Basic inventory manager with SQLite | [`inventario_sqlite.py`](<Ejercicios Intermedio/inventario_sqlite.py>) |
| 18 | ✅ Real-time chat application (Sockets) | [`Aplicación de Chat con Sockets/`](<Ejercicios Intermedio/Aplicación de Chat con Sockets>) |
| 19 | ✅ Basic image editor (filters and resizing) | [`Editor de imágenes básico/`](<Ejercicios Intermedio/Editor de imágenes básico>) |
| 20 | ✅ Cryptocurrency data viewer (API) | [`visualizador_cripto.py`](<Ejercicios Intermedio/visualizador_cripto.py>) |
| 21 | ✅ Snake game with Pygame | [`juego_snake.py`](<Ejercicios Intermedio/juego_snake.py>) |
| 23 | ✅ Notes app with user login | [`notas_seguras.py`](<Ejercicios Intermedio/notas_seguras.py>) |
| 24 | ✅ Simple electronic voting system | [`sistema_votacion.py`](<Ejercicios Intermedio/sistema_votacion.py>) |
| 25 | ⏳ Text sentiment analyzer | — |
| 26 | ⏳ Email automation | — |
| 27 | ⏳ Quiz app with API | — |

### 🔴 Advanced Level — Structural Algorithms

| # | Project | File |
| --- | --- | --- |
| 28 | ⏳ Movie recommendation system (Pandas / Math) | — |
| 29 | ⏳ Blockchain from scratch (block simulation) | — |
| 30 | ⏳ Network traffic analyzer (Scapy sniffer) | — |
| 31 | ⏳ File compressor (Huffman algorithm) | — |
| 32 | ⏳ HTTP web server from scratch (raw sockets) | — |
| 33 | ⏳ Chess game with AI (Minimax algorithm) | — |
| 34 | ⏳ Full-text search engine (inverted index) | — |
| 35 | ⏳ Optimal route planner (Dijkstra's algorithm) | — |

### 🛡️ Cybersecurity — Local Scripts & Tools

| # | Project | File |
| --- | --- | --- |
| 36 | ⏳ Local password manager with encryption | — |
| 37 | ▶️ Basic port scanner (file created / active testing) | [`Escaner De Puertos.py`](<Ejercicios Avanzado/Escaner De Puertos.py>) |
| 38 | ⏳ Keylogger (educational use only) | — |
| 39 | ⏳ Phishing page simulator (temporary local server) | — |
| 40 | ⏳ Rule-based basic firewall (IP blocking) | — |
| 41 | ⏳ Secure chat app (end-to-end encryption) | — |
| 42 | ⏳ Penetration testing automation script | — |
| 43 | ⏳ Cryptography tool (AES / RSA encryption and decryption) | — |

> ⚠️ All security tools in this repository are for educational purposes and are only run on my own machines or on systems I have explicit permission to test.
