# 🔐 Password Strength Checker

A beautiful, colorful, and advanced **Password Strength Analyzer** built using Python. This interactive CLI tool evaluates password strength using multiple metrics such as length, complexity, entropy, and common password detection — all enhanced with color-coded output and stylish ASCII banners for an engaging user experience.

---

## ✨ Features

- 🎨 **Colorful Terminal UI** (uses `termcolor` and `pyfiglet`)
- 🔍 **Multi-Factor Strength Analysis**:
  - Password length assessment
  - Character diversity check (uppercase, lowercase, digits, symbols)
  - Detection of common passwords
  - Entropy calculation (bit-level strength)
- 📊 **Visual strength meter** (0–10)
- 📝 **Detailed feedback** on each factor
- 🔁 **Retry option** for testing multiple passwords
- 🛡 Graceful exit on keyboard interrupt (Ctrl+C)
- 🔒 Secure password input using `getpass` (no echo)

---


## 🚀 Getting Started

### 🔧 Prerequisites

Ensure Python 3.x is installed. Then, install dependencies:

```bash
pip install termcolor pyfiglet
