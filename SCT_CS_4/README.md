# ⌨️ Advanced Keylogger with Colorful Logging (Python)

A **Python-based Keylogger** that captures keyboard keystrokes and logs them to a file with timestamped entries. Built using the `pynput`, `colorama`, `logging`, and `datetime` modules, this project provides a clear, color-enhanced command-line interface for better visibility and tracking of user input.

> ⚠️ **Disclaimer:** This project is intended strictly for **educational** and **ethical** purposes only. Using this tool to log keystrokes without informed consent is illegal and unethical. Always comply with local laws and regulations regarding monitoring tools.

---

## 📌 Project Overview

This keylogger captures both **alphanumeric** and **special keys** (like Enter, Shift, etc.), logging each keystroke along with a timestamp to a local log file (`enhanced_keylog.txt`). The tool also prints colored messages to the terminal to distinguish between key types in real time.

---

## 🎯 Features

- ✅ Logs every key pressed, including special keys (e.g., `Backspace`, `Space`, `Shift`)
- 🕒 Timestamped logging using Python’s `logging` module
- 🖍️ Color-coded terminal output for better visibility using `colorama`
- 📁 Saves logs to a local file: `enhanced_keylog.txt`
- 🚨 Gracefully exits when `ESC` is pressed
- 🔒 Tracks keystroke count per session

---

## 🧰 Technologies Used

- **Python 3.x**
- **pynput** – to capture keyboard input
- **colorama** – for colorful terminal output
- **logging** – for log file generation
- **datetime & os** – for session handling

---


