# 🖼️ Simple Image Encryption Tool using Pixel Manipulation

A Python-based utility that encrypts and decrypts images using basic **pixel value manipulation**. This project demonstrates how simple mathematical operations on pixel data can obscure image content, serving as a foundational concept in visual cryptography and steganography.

---

## 🔐 Project Overview

This tool applies a basic **encryption algorithm** that manipulates RGB pixel values to make the image unreadable to the naked eye. The original image can be restored using the reverse operation (decryption).

> ⚠️ Note: This is a simple educational project and **should not be used for real-world security or privacy needs**. It's ideal for beginners learning about image processing and cryptographic logic.

---

## 🧰 Technologies Used

- **Python 3.x**
- **Pillow (PIL)** – For image loading and pixel manipulation
- **Colorama (optional)** – For colored CLI output
- **OS, datetime, and logging** – For file handling and logging session data

---

## ✨ Features

- 🔒 Encrypts an image by manipulating RGB values
- 🔓 Decrypts back to the original using inverse logic
- 📁 Supports `.png`, `.jpg`, `.jpeg`, and other formats supported by Pillow
- 📜 Logs actions and status to a log file
- 🌈 CLI-based, interactive, and colorful output using `colorama`

---

## 🖼️ How It Works

The core idea is to **modify each pixel** by applying a reversible transformation. For example:

```python
# Encryption
r_new = 255 - r
g_new = 255 - g
b_new = 255 - b

# Decryption (invert again)
r_original = 255 - r_new
g_original = 255 - g_new
b_original = 255 - b_new
