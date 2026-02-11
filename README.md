# Python GUI Projects

Welcome to the **Python GUI Projects** collection! This repository hosts a variety of interactive desktop applications utilizing **Python**, **Tkinter**, and **Turtle** graphics. From classic arcade games to practical productivity tools, this workspace showcases different GUI development patterns and techniques.

## 📂 Project Overview

### 1. Pong Game (`GUI1`)

A recreation of the classic **Pong** arcade game.

- **Tech Stack**: Python, Turtle Graphics.
- **Description**: A two-player game where opponents control paddles to bounce a ball back and forth. The game tracks scores and increases ball speed for added difficulty.
- **Controls**:
  - **Right Paddle**: `Up` / `Down` arrows
  - **Left Paddle**: `w` / `s` keys

### 2. Turtle Crossing (`GUI2`)

A "Frogger"-style arcade game.

- **Tech Stack**: Python, Turtle Graphics.
- **Description**: The player controls a turtle that must cross a busy road filled with moving cars. The goal is to reach the other side without colliding. Levels get progressively harder as car speed increases.
- **Controls**:
  - **Move**: `Up` arrow

### 3. Mile to Kilometer Converter (`convert_miles_to_km`)

A handy utility for unit conversion.

- **Tech Stack**: Python, Tkinter.
- **Description**: A clean and simple GUI that allows users to input a distance in miles and instantly see the equivalent in kilometers.

### 4. Flash Card App (`flash-card-project-start`)

A language learning assistant.

- **Tech Stack**: Python, Tkinter, Pandas.
- **Description**: An application designed to help learn new languages (e.g., French/English) using flashcards. It displays a word, waits for a few seconds, and then flips the card to reveal the translation.
- **Features**:
  - Auto-flipping cards.
  - Tracking of known vs. unknown words to optimize learning.

### 5. Password Manager (`password_manager`)

A secure tool for managing credentials.

- **Tech Stack**: Python, Tkinter.
- **Description**: A local password manager that generates strong, random passwords and saves them along with your email and website details.
- **Features**:
  - **Password Generator**: Creates complex passwords with a mix of letters, numbers, and symbols.
  - **Search**: Quickly retrieve saved passwords for specific websites.
  - **Storage**: JSON-based local storage.

### 6. Pomodoro Timer (`pomodoro_GUI`)

A focus timer based on the Pomodoro Technique.

- **Tech Stack**: Python, Tkinter.
- **Description**: A productivity tool that alternates between 25-minute work sessions and short breaks to keep you focused and fresh.
- **Features**:
  - Visual countdown timer.
  - Checkmarks to track completed sessions.

---

## 🚀 Getting Started

To run any of these projects, ensure you have **Python 3.x** installed.

1.  **Clone the repository** (or download the files):

    ```bash
    git clone <your-repo-url>
    cd Back-end/GUI
    ```

2.  **Navigate to a project folder**:

    ```bash
    cd password_manager
    ```

3.  **Run the application**:
    ```bash
    python main.py
    ```

## 🛠️ Prerequisites

Most projects rely on standard Python libraries (`tkinter`, `turtle`, `random`, `time`).
Some projects (like the Flash Card App) may require:

- `pandas`

Install dependencies if prompted:

```bash
pip install pandas
```

## 📜 License

This project is for educational purposes. Feel free to modify and improve the code!
