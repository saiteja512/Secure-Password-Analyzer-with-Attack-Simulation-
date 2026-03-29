# 🔐 Secure Password Analyzer with Attack Simulation

## 📌 Project Description

The **Secure Password Analyzer** is a desktop application developed
using Python that evaluates the strength of a password and estimates the
time required to crack it using a brute-force attack simulation.

This project demonstrates core **Data Structures and Algorithms (DSA)**
concepts along with cybersecurity principles such as hashing, pattern
matching, and complexity analysis. The system helps users understand how
secure their passwords are and provides suggestions for improvement.

------------------------------------------------------------------------

## 🎯 Project Objective

-   Analyze password strength using predefined security rules
-   Demonstrate secure password storage using hashing
-   Simulate brute-force attack time estimation
-   Provide recommendations to improve password security
-   Apply DSA concepts in a real-world cybersecurity problem

------------------------------------------------------------------------

## ⚙️ Key Features

-   Password strength evaluation
-   SHA-256 hashing implementation
-   Brute-force attack simulation
-   Crack time estimation
-   Suggestions for password improvement
-   Show / Hide password functionality
-   Simple and user-friendly GUI interface
-   Edge-case handling (No suggestions message)

------------------------------------------------------------------------

## 🧠 DSA Concepts Used

  DSA Concept             Implementation
  ----------------------- ---------------------------
  Strings                 Password input processing
  Hashing                 SHA-256 algorithm
  Pattern Matching        Regex validation
  Brute Force Algorithm   Attack simulation logic
  Time Complexity         Combination calculation
  Conditional Logic       Strength scoring system

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Programming Language: Python 3
-   GUI Framework: Tkinter
-   Libraries:
    -   tkinter
    -   ttk
    -   re (Regular Expressions)
    -   hashlib

------------------------------------------------------------------------

## 🧩 System Workflow

1.  User enters a password.
2.  Program checks password rules:
    -   Minimum length
    -   Uppercase letters
    -   Lowercase letters
    -   Numbers
    -   Special characters
3.  Password strength score is calculated.
4.  Password is converted into a SHA-256 hash.
5.  Character set size is determined.
6.  Possible combinations are calculated.
7.  Estimated brute-force crack time is displayed.
8.  Suggestions are shown if improvements are needed.

------------------------------------------------------------------------

## 🔐 Password Strength Criteria

  Rule        Description
  ----------- -----------------------------
  Length      Minimum 8 characters
  Uppercase   At least one capital letter
  Lowercase   At least one small letter
  Numbers     At least one digit
  Symbols     Special characters required

------------------------------------------------------------------------

## ⏱️ Crack Time Calculation

Total Combinations = (Character Set Size) \^ Password Length\
Crack Time = Total Combinations / Guesses Per Second

Assumption: - Attacker speed = **1 billion guesses per second**

------------------------------------------------------------------------

## 📊 Time Complexity Analysis

  Operation                Complexity
  ------------------------ ------------
  Password scanning        O(n)
  Regex matching           O(n)
  Hash generation          O(n)
  Crack time calculation   O(1)

Overall Complexity: **O(n)**

------------------------------------------------------------------------

## 🚀 How to Run the Project

### Step 1: Install Python

Download Python from: https://www.python.org/downloads/

Enable: Add Python to PATH

### Step 2: Download Project

Place the file: Secure_password_Analyzer.py

### Step 3: Run Program

Open terminal in project folder and run: python Secure_password_Analyzer.py

The GUI window will open.

------------------------------------------------------------------------

## 🖥️ User Interface Components

-   Password Input Field
-   Show / Hide Password Button
-   Analyze Button
-   Strength Indicator
-   Progress Bar
-   Crack Time Display
-   SHA-256 Hash Output
-   Suggestions Panel

------------------------------------------------------------------------

## 🌍 Real-World Applications

-   Authentication systems
-   Banking applications
-   Password managers
-   Cybersecurity awareness tools
-   Account security validation systems

------------------------------------------------------------------------

## 🔮 Future Enhancements

-   Password entropy calculation
-   Dictionary attack detection
-   Real-time strength analysis while typing
-   Web-based implementation (Flask/Django)
-   Database storage for password reports
-   AI-based password pattern prediction

------------------------------------------------------------------------

## 🧪 Testing

Tested using: - Weak passwords - Medium-strength passwords - Strong
passwords - Edge cases (empty input, minimal characters)

------------------------------------------------------------------------

## 📁 Project Structure

Project Folder/ │ ├── Secure_password_Analyzer.py └── README.md

------------------------------------------------------------------------

## 👨‍💻 Author
Saiteja Mareda
Santhosh Daravath
Greeshma Mukera

Secure_password_Analyzer Project\
Secure Password Analyzer with Attack Simulation

------------------------------------------------------------------------

## 📄 License

This project is developed for academic and educational purposes only.
