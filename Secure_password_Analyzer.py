import tkinter as tk
from tkinter import ttk, messagebox
import hashlib
import re

def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    minutes = seconds / 60
    if minutes < 60:
        return f"{minutes:.2f} minutes"
    hours = minutes / 60
    if hours < 24:
        return f"{hours:.2f} hours"
    days = hours / 24
    if days < 365:
        return f"{days:.2f} days"
    years = days / 365
    return f"{years:.2e} years"

def analyze_password():
    password = password_entry.get()

    if password.strip() == "":
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    password = password.strip()
    suggestions = []
    length = len(password)

    if length < 8:
        suggestions.append("Use at least 8 characters")

    if not re.search(r"[A-Z]", password):
        suggestions.append("Add uppercase letters")

    if not re.search(r"[a-z]", password):
        suggestions.append("Add lowercase letters")

    if not re.search(r"\d", password):
        suggestions.append("Add numbers")

    if not re.search(r"[!@#$%^&*()_\-+=\[\]{};:'\",.<>/?\\|`~]", password):
        suggestions.append("Add special characters")

    if len(set(password)) <= 2:
        suggestions.append("Avoid repeated characters")

    score = 0

    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*()_\-+=\[\]{};:'\",.<>/?\\|`~]", password):
        score += 1

    if len(set(password)) <= 2:
        score -= 1

    score = max(score, 0)

    if score <= 1:
        strength = "Very Weak"
        progress["value"] = 15
    elif score == 2:
        strength = "Weak"
        progress["value"] = 30
    elif score == 3:
        strength = "Moderate"
        progress["value"] = 50
    elif score == 4:
        strength = "Strong"
        progress["value"] = 70
    elif score == 5:
        strength = "Very Strong"
        progress["value"] = 85
    else:
        strength = "Excellent"
        progress["value"] = 100

    strength_label.config(text=f"Password Strength: {strength}")

    sha256_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    hash_output.config(text=sha256_hash)

    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"\d", password):
        charset += 10
    if re.search(r"[^\w\s]", password):
        charset += 32

    charset = max(charset, 1)

    guesses_per_sec = 1e9

    try:
        combinations = charset ** length
        crack_time = combinations / guesses_per_sec
        crack_time_text = format_time(crack_time)
    except OverflowError:
        crack_time_text = "Extremely Large"

    crack_time_label.config(text=f"Estimated Crack Time: {crack_time_text}")

    suggestion_box.delete("1.0", tk.END)

    if not suggestions:
        suggestion_box.insert(tk.END, "No suggestions")
    else:
        for s in suggestions:
            suggestion_box.insert(tk.END, f"• {s}\n")

def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        toggle_btn.config(text="Show")
    else:
        password_entry.config(show="")
        toggle_btn.config(text="Hide")

root = tk.Tk()
root.title("Secure Password Analyzer")
root.geometry("600x520")
root.configure(bg="#0f172a")

title = tk.Label(
    root,
    text="🔐 Secure Password Analyzer",
    font=("Arial", 18, "bold"),
    bg="#0f172a",
    fg="white",
)
title.pack(pady=15)

frame = tk.Frame(root, bg="#0f172a")
frame.pack()

password_entry = tk.Entry(frame, width=30, font=("Arial", 14), show="*")
password_entry.grid(row=0, column=0, padx=5)

toggle_btn = tk.Button(
    frame, text="Show", command=toggle_password, bg="#22c55e", fg="white"
)
toggle_btn.grid(row=0, column=1)

analyze_btn = tk.Button(
    root,
    text="Analyze Password",
    command=analyze_password,
    bg="#2563eb",
    fg="white",
    font=("Arial", 12, "bold"),
)
analyze_btn.pack(pady=15)

strength_label = tk.Label(
    root, text="", font=("Arial", 13), bg="#0f172a", fg="white"
)
strength_label.pack()

progress = ttk.Progressbar(root, length=300)
progress.pack(pady=10)

tk.Label(root, text="SHA-256 Hash:", bg="#0f172a", fg="white").pack()

hash_output = tk.Label(
    root, text="", wraplength=500, bg="#0f172a", fg="#38bdf8"
)
hash_output.pack(pady=5)

crack_time_label = tk.Label(
    root, text="", bg="#0f172a", fg="white", font=("Arial", 11)
)
crack_time_label.pack(pady=10)

tk.Label(root, text="Suggestions:", bg="#0f172a", fg="white").pack()

suggestion_box = tk.Text(root, height=6, width=55)
suggestion_box.pack(pady=10)

root.mainloop()
