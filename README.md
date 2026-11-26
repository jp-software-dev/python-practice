# Python Practice 🐍

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Pygame](https://img.shields.io/badge/pygame-2E7D32?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/tkinter-GUI-blue?style=for-the-badge)

My personal Python practice repository. It collects the scripts I write to build programming logic step by step: course notes, a 100-day challenge, and small projects grouped by level — from simple console games to SQLite apps, sockets, web scraping and security tools.

Every script is standalone: open the file and run it. Nothing here depends on another folder.

> **Learning path:** this repo follows a roadmap that keeps growing. See [Roadmap](#-roadmap) for what is done and what comes next.

## 📁 What's inside

| Folder | Content |
| --- | --- |
| [`Curso Python/`](<Curso Python>) | Course fundamentals: variables, input, type conversion, strings and string methods, indexing, lists and 2D lists, tuples, sets, dictionaries, `if`, `for` / `while` loops, `break` / `continue`, math functions and a Caesar cipher. |
| [`Reto de 100 Dias/`](<Reto de 100 Dias>) | 100 Days of Code challenge (`P1.py` → `P99.py`): one short exercise per day, going from arithmetic and string slicing to loops, functions, `lambda` / `map`, classes and system info with `psutil`. |
| [`Ejercicios Principiante/`](<Ejercicios Principiante>) | Beginner projects: games, calculators, converters, clocks, a To-Do list, a file organizer and small API clients. |
| [`Ejercicios Intermedio/`](<Ejercicios Intermedio>) | Intermediate projects: SQLite apps, web scraping, a socket chat, an image editor, a crypto price viewer, Snake with Pygame, secure notes and a voting system. Also includes `Ejercicios con Sockets/`, a set of TCP, UDP, raw ICMP, DNS and XML-RPC exercises. |
| [`Ejercicios Avanzado/`](<Ejercicios Avanzado>) | Advanced projects: a multithreaded port scanner and a Tkinter calendar. |
| [`Qr-Enlaces/`](Qr-Enlaces), [`Qr-Imagenes/`](Qr-Imagenes), [`Qr-Texto/`](Qr-Texto) | QR code generators for links, images and plain text. |
| [`Analisis de Datos/`](<Analisis de Datos>) | Datasets for upcoming data analysis practice (wine chemical-composition dataset). |

## 🗺️ Roadmap

✅ Done · ▶️ In progress · ⏳ Planned

### 🟢 Beginner — completed

| # | Project | File |
| --- | --- | --- |
| 1 | ✅ Tip calculator | [`Calculadora de propinas.py`](<Ejercicios Principiante/Calculadora de propinas.py>) |
| 2 | ✅ Rock, paper, scissors | [`Juego Clasico.py`](<Ejercicios Principiante/Juego Clasico.py>) |
| 3 | ✅ Digital clock with GUI (Tkinter) | [`Reloj Digital.py`](<Ejercicios Principiante/Reloj Digital.py>) |
| 4 | ✅ Simple link shortener (TinyURL API) | [`Acortador de enlaces.py`](<Ejercicios Principiante/Acortador de enlaces.py>) |
| 5 | ✅ File organizer by extension | [`Organizador de archivos.py`](<Ejercicios Principiante/Organizador de archivos.py>) |
| 6 | ✅ Word counter | [`Contador de palabras.py`](<Ejercicios Principiante/Contador de palabras.py>) |
| 7 | ✅ Unit converter (Celsius ↔ Fahrenheit) | [`Convertidor de unidades.py`](<Ejercicios Principiante/Convertidor de unidades.py>) |
| 8 | ✅ To-Do list | [`Lista de tareas pendientes.py`](<Ejercicios Principiante/Lista de tareas pendientes.py>) |
| 9 | ✅ Dice roll simulator | [`Lanzamiento de dados..py`](<Ejercicios Principiante/Lanzamiento de dados..py>) |
| 10 | ✅ Countdown timer (Pomodoro) | [`Reloj de cuenta regresiva.py`](<Ejercicios Principiante/Reloj de cuenta regresiva.py>) |
| 11 | ✅ Dictionary definition finder (API) | [`Buscador de definiciones diccionario.py`](<Ejercicios Principiante/Buscador de definiciones diccionario.py>) |
| 12 | ✅ Palindrome checker | [`Verificador de palíndromo.py`](<Ejercicios Principiante/Verificador de palíndromo.py>) |
| 13 | ✅ Current weather notifier (wttr.in) | [`Notificador de clima actual.py`](<Ejercicios Principiante/Notificador de clima actual.py>) |
| 14 | ✅ Hangman | [`Juego del ahorcado.py`](<Ejercicios Principiante/Juego del ahorcado.py>) |

Extra beginner scripts: number guessing game, password generator (`secrets`), RPG character classes, ASCII figures, a colored heart (`colorama`), a terminal "music" player and a first Tkinter window.

### 🟡 Intermediate — in progress

| # | Project | File |
| --- | --- | --- |
| 15 | ✅ Web scraper for book prices (`requests` + BeautifulSoup) | [`web_scraper.py`](<Ejercicios Intermedio/web_scraper.py>) |
| 16 | ✅ URL shortener with SQLite | [`acortador_sqlite.py`](<Ejercicios Intermedio/acortador_sqlite.py>) |
| 17 | ✅ Inventory manager with SQLite (CRUD) | [`inventario_sqlite.py`](<Ejercicios Intermedio/inventario_sqlite.py>) |
| 18 | ✅ Real-time chat with sockets and threads | [`Aplicación de Chat con Sockets/`](<Ejercicios Intermedio/Aplicación de Chat con Sockets>) |
| 19 | ✅ Basic image editor (filters and resize with Pillow) | [`Editor de imágenes básico/`](<Ejercicios Intermedio/Editor de imágenes básico>) |
| 20 | ✅ Crypto price viewer (CoinGecko API) | [`visualizador_cripto.py`](<Ejercicios Intermedio/visualizador_cripto.py>) |
| 21 | ✅ Snake game with Pygame | [`juego_snake.py`](<Ejercicios Intermedio/juego_snake.py>) |
| 23 | ✅ Notes app with user login (SHA-256 password hashing) | [`notas_seguras.py`](<Ejercicios Intermedio/notas_seguras.py>) |
| 24 | ✅ Simple voting system (one vote per ID) | [`sistema_votacion.py`](<Ejercicios Intermedio/sistema_votacion.py>) |
| 25 | ⏳ Text sentiment analyzer | — |
| 26 | ⏳ Email automation | — |
| 27 | ⏳ Quiz app with an API | — |

### 🔴 Advanced — algorithms

| # | Project | File |
| --- | --- | --- |
| 28 | ⏳ Movie recommendation system (Pandas) | — |
| 29 | ⏳ Blockchain from scratch (block simulation) | — |
| 30 | ⏳ Network traffic analyzer (sniffer with Scapy) | — |
| 31 | ⏳ File compressor (Huffman coding) | — |
| 32 | ⏳ HTTP web server from scratch (raw sockets) | — |
| 33 | ⏳ Chess with AI (Minimax) | — |
| 34 | ⏳ Full-text search engine (inverted index) | — |
| 35 | ⏳ Shortest route planner (Dijkstra) | — |

### 🛡️ Cybersecurity — local scripts and tools

| # | Project | File |
| --- | --- | --- |
| 36 | ⏳ Local password manager with encryption | — |
| 37 | ▶️ Basic port scanner (multithreaded) | [`Escaner De Puertos.py`](<Ejercicios Avanzado/Escaner De Puertos.py>) |
| 38 | ⏳ Keylogger (educational use only) | — |
| 39 | ⏳ Phishing page simulator (temporary local server, for awareness training) | — |
| 40 | ⏳ Rule-based basic firewall (IP blocking) | — |
| 41 | ⏳ Secure chat app (end-to-end encryption) | — |
| 42 | ⏳ Penetration testing automation script | — |
| 43 | ⏳ Cryptography tool (AES / RSA) | — |

> The security tools are for learning and must only be used on my own machines or on systems I have explicit permission to test.

## 💻 Tech used so far

| Area | Libraries |
| --- | --- |
| Core | Python 3 standard library: `os`, `shutil`, `json`, `random`, `secrets`, `math`, `time`, `calendar` |
| GUI and games | `tkinter`, `pygame` |
| Databases | `sqlite3` |
| Networking | `socket`, `threading`, `xmlrpc` |
| Web and APIs | `requests`, `beautifulsoup4` (TinyURL, wttr.in, CoinGecko, dictionary API, books.toscrape.com) |
| Security | `hashlib` (SHA-256), `getpass`, Caesar cipher |
| Images and QR | `Pillow`, `qrcode` |
| System and terminal | `psutil`, `colorama` |

## 🚀 Run the scripts

Requirements: Python 3.10 or newer.

```bash
git clone https://github.com/jp-software-dev/python-practice.git
cd python-practice
```

Most scripts only use the standard library. For the rest, install the third-party packages once:

```bash
pip install requests beautifulsoup4 "qrcode[pil]" pillow pygame psutil colorama
```

Then run any file. Use quotes because many paths have spaces:

```bash
python "Ejercicios Intermedio/juego_snake.py"
```

For the socket chat, start `servidor.py` first and then one or more `cliente.py` in other terminals.
