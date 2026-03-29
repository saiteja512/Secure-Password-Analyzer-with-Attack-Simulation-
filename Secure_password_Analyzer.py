import tkinter as tk
from tkinter import ttk
import re
import hashlib


def check_password_rules(pwd):
    points = 0
    tips = []

    if len(pwd) >= 8:
        points += 1
    else:
        tips.append("Password should contain at least 8 characters")

    if re.search(r"[A-Z]", pwd):
        points += 1
    else:
        tips.append("Add an uppercase letter")

    if re.search(r"[a-z]", pwd):
        points += 1
    else:
        tips.append("Add a lowercase letter")

    if re.search(r"\d", pwd):
        points += 1
    else:
        tips.append("Include numbers")

    if re.search(r"[!@#$%^&*]", pwd):
        points += 1
    else:
        tips.append("Use special symbols")

    return points, tips



def create_hash(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()



def estimate_crack_time(pwd):
    charset_size = 0

    if re.search(r"[a-z]", pwd):
        charset_size += 26
    if re.search(r"[A-Z]", pwd):
        charset_size += 26
    if re.search(r"\d", pwd):
        charset_size += 10
    if re.search(r"[!@#$%^&*]", pwd):
        charset_size += 32

    if charset_size == 0:
        return "Instant"

    total_guess = charset_size ** len(pwd)
    guesses_per_second = 1e9

    seconds = total_guess / guesses_per_second

    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    else:
        return f"{seconds/86400:.2f} days"



def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        toggle_btn.config(text="Hide Password")
    else:
        password_entry.config(show="*")
        toggle_btn.config(text="Show Password")



def analyze_password():
    pwd = password_entry.get()

    score, tips = check_password_rules(pwd)
    hashed_pwd = create_hash(pwd)
    crack_time = estimate_crack_time(pwd)

    levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong", "Excellent"]

    result_label.config(text=f"Strength: {levels[score]}")
    progress_bar['value'] = score * 20

    hash_label.config(text="SHA-256: " + hashed_pwd[:45] + "...")
    time_label.config(text="Crack Time: " + crack_time)

    tips_box.delete(0, tk.END)

    if len(tips) == 0:
        tips_box.insert(tk.END, "No suggestions — Your password is strong ✅")
    else:
        for t in tips:
            tips_box.insert(tk.END, t)



app = tk.Tk()
app.title("Password Security Analyzer")
app.geometry("620x520")
app.configure(bg="#1e1e2f")   

title = tk.Label(app,
                 text="Password Security Analyzer",
                 font=("Helvetica", 18, "bold"),
                 fg="white",
                 bg="#1e1e2f")
title.pack(pady=15)

password_entry = tk.Entry(app,
                          width=32,
                          font=("Helvetica", 14),
                          show="*",
                          justify="center")
password_entry.pack(pady=10)

toggle_btn = tk.Button(app,
                       text="Show Password",
                       command=toggle_password,
                       bg="#ff9800",
                       fg="white")
toggle_btn.pack(pady=5)

analyze_btn = tk.Button(app,
                        text="Analyze",
                        command=analyze_password,
                        font=("Helvetica", 12, "bold"),
                        bg="#4caf50",
                        fg="white",
                        width=15)
analyze_btn.pack(pady=12)

result_label = tk.Label(app,
                        text="Strength:",
                        font=("Helvetica", 14),
                        fg="white",
                        bg="#1e1e2f")
result_label.pack()

progress_bar = ttk.Progressbar(app, length=300, maximum=100)
progress_bar.pack(pady=10)

time_label = tk.Label(app,
                      text="Crack Time:",
                      fg="white",
                      bg="#1e1e2f",
                      font=("Helvetica", 12))
time_label.pack(pady=5)

hash_label = tk.Label(app,
                      text="SHA-256:",
                      wraplength=520,
                      fg="#00e5ff",
                      bg="#1e1e2f")
hash_label.pack(pady=10)


tk.Label(app,
         text="Suggestions",
         font=("Helvetica", 12, "bold"),
         fg="white",
         bg="#1e1e2f").pack()

tips_box = tk.Listbox(app, width=55, height=6)
tips_box.pack(pady=10)

app.mainloop()