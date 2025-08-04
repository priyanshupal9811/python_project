# 🌡️ Temperature Converter

This Python project converts temperature between Celsius, Fahrenheit, and Kelvin.

## 🔧 Features
- Convert between:
  - Celsius ↔ Fahrenheit
  - Celsius ↔ Kelvin
  - Fahrenheit ↔ Kelvin

## 🚀 How to Run
```bash
python temperature_converter.py

📝 Example

Enter temperature in Celsius: 100
100°C = 212°F
100°C = 373.15K

---

## 📁 `Guess_game/README.md`

```markdown
# 🎯 Guess the Number Game

A simple Python game where the user tries to guess a randomly generated number.

## 🎮 Features
- Random number between 1 and 100
- Tells the user if their guess is too high or too low
- Counts number of attempts

## 🚀 How to Run
```bash
python guess_game.py

📝 Example

Guess a number between 1 and 100: 50
Too low!
...
You guessed it in 6 tries!

---

## 📁 `Solving_suduko/README.md`

```markdown
# 🧩 Sudoku Solver

This Python script solves a 9x9 Sudoku puzzle using backtracking algorithm.

## 🧠 Features
- Input puzzle as a 2D grid
- Fills in missing numbers
- Validates the solution

## 🚀 How to Run
```bash
python solving_sudoku.py

📝 Example Grid

530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079

📤 Output

Displays the solved Sudoku grid in the terminal.

---

## 📁 `password_strength_checker/README.md`

```markdown
# 🔐 Password Strength Checker

Checks how strong a password is and gives suggestions. Saves results to a CSV file.

## ✅ Features
- Checks:
  - Length
  - Upper/lowercase letters
  - Digits
  - Special characters
  - Weak patterns like "123", "password", etc.
- Gives strength score out of 10
- Saves results to `password_check_log.csv`

## 🚀 How to Run
```bash
python password_checker.py

📝 Example Output

Enter your password: Hello@123

Password Strength: Strong 💪 (8/10)

✅ Result saved to 'password_check_log.csv'

---

## 🧾 Main `requirements.txt` (for entire `python_project`)

If you're using libraries like `re`, `csv`, `datetime`, they’re all built-in.  
But if in future you add external libraries, your `requirements.txt` can look like this:

```txt
# All used libraries so far are built-in.
# If you add more, list them here. Example:
# pandas
# requests
# beautifulsoup4
