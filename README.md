# 🔐 Secure Password Analyzer with Attack Simulation

## 📌 Project Description

The **Secure Password Analyzer** is a desktop application developed
using **Python** that evaluates password strength and estimates the time
required to crack it using a brute-force attack simulation.

This project demonstrates core **Data Structures and Algorithms (DSA)**
concepts along with cybersecurity principles such as hashing, pattern
matching, and complexity analysis.

------------------------------------------------------------------------

## 🎯 Project Objectives

-   Analyze password strength using security rules
-   Demonstrate secure password storage using hashing
-   Simulate brute-force attack time estimation
-   Provide recommendations for stronger passwords
-   Apply DSA concepts in a real-world cybersecurity problem

------------------------------------------------------------------------

## ⚙️ Key Features

-   Password strength evaluation
-   SHA-256 hashing implementation
-   Brute-force attack simulation
-   Crack time estimation
-   Password improvement suggestions
-   Show / Hide password functionality
-   User-friendly GUI interface
-   Displays **"No suggestions"** when password is strong

------------------------------------------------------------------------

## 🧠 DSA Concepts Used

  DSA Concept             Implementation
  ----------------------- ---------------------------
  Strings               -  Password input processing
  
  Hashing               -  SHA-256 algorithm
  
  Pattern Matching      - Regex validation
  
  Brute Force Algorithm -  Attack simulation logic
  
  Time Complexity       - Combination calculation
  
  Conditional Logic     -  Strength scoring

------------------------------------------------------------------------

## 🛠️ Technologies Used

**Programming Language** - Python 3

**GUI Framework** - Tkinter

**Libraries** - tkinter - ttk - re (Regular Expressions) - hashlib

------------------------------------------------------------------------

## 🧩 System Workflow

1.  User enters a password.
2.  Program checks:
    -   Minimum length
    -   Uppercase letters
    -   Lowercase letters
    -   Numbers
    -   Special characters
3.  Password strength score is calculated.
4.  Password is converted into a SHA-256 hash.
5.  Character set size is determined.
6.  Possible combinations are calculated.
7.  Estimated crack time is displayed.
8.  Suggestions are shown if required.

------------------------------------------------------------------------

## 🔐 Password Strength Criteria

  Rule        Description
  ----------- -----------------------------
  Length     - Minimum 8 characters
  
  Uppercase  - At least one capital letter 
  
  Lowercase  - At least one small letter
  
  Numbers    - At least one digit
  
  Symbols    - Special characters required

------------------------------------------------------------------------

## ⏱️ Crack Time Calculation

    Total Combinations = (Character Set Size) ^ Password Length
    Crack Time = Total Combinations / Guesses Per Second

**Assumption:**\
Attacker speed = **1 Billion guesses per second**

------------------------------------------------------------------------

## 📊 Time Complexity Analysis

  Operation                Complexity
  ------------------------ ------------
  Password scanning      -   O(n)
  
  Regex matching         -   O(n)
  
  Hash generation        -   O(n)
   
  Crack time calculation -   O(1)

**Overall Complexity:** `O(n)`

------------------------------------------------------------------------

## 🚀 How to Run the Project

### Step 1: Install Python

Download Python from: https://www.python.org/downloads/

✔ Enable **Add Python to PATH**

### Step 2: Install Requirements

    pip install -r requirements.txt

### Step 3: Run Program

    python Secure_password_Analyzer.py

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
-   Real-time strength analysis
-   Web-based version (Flask/Django)
-   Database storage for reports
-   AI-based password pattern prediction

------------------------------------------------------------------------

## 🧪 Testing

Tested using: - Weak passwords - Medium passwords - Strong passwords -
Empty input cases - Edge cases

------------------------------------------------------------------------

## 📁 Project Structure

    Secure-Password-Analyzer/
    │
    ├── Secure_password_Analyzer.py
    ├── README.md
    ├── requirements.txt
    └── .gitignore

------------------------------------------------------------------------

## 👨‍💻 Authors

-   Saiteja Mareda
-   Santhosh Daravath
-   Greeshma Mukera

------------------------------------------------------------------------

## 📄 License

This project is developed for **academic and educational purposes
only**.
