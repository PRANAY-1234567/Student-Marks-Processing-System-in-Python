# 📊 Student Marks Processing System in Python (OOP)

## 📌 Description

This Python program implements a **Student Marks Management System** using **Object-Oriented Programming (OOP)**. It calculates total marks, percentage, result (Pass/Fail), and assigns a grade based on performance.

---

## 🚀 Features

* Stores student details (roll number, name, marks)
* Calculates:

  * Total marks
  * Percentage
* Determines:

  * Pass/Fail status
  * Grade (First, Second, Third)
* Highlights failed subjects (marks < 40)
* Displays a formatted report

---

## 🛠️ How It Works

1. A class `MarksData` is created with attributes:

   * `roll`, `name`, `marks`
   * `total`, `percent`, `result`, `grade`

2. Methods:

   * `setMarksData()` → Assigns student details
   * `process()` →

     * Calculates total and percentage
     * Checks if any subject is below 40 → Fail
     * Assigns grade:

       * ≥ 80 → First
       * ≥ 60 → Second
       * < 60 → Third
       * Fail → `*`
   * `displayMarksData()` → Prints formatted result

3. The main program:

   * Creates object `ms`
   * Sets data
   * Processes and displays result

---

## 💻 Code

```python id="d9x4pl"
class MarksData:
    def __init__(self):
        self.roll = 0
        self.name = ""
        self.marks = []
        self.total = 0
        self.percent = 0.0
        self.result = ""
        self.grade = ""

    def setMarksData(self, rn, nm, mrk):
        self.roll = rn
        self.name = nm
        self.marks = mrk

    def process(self):
        self.total = 0
        self.result = "Pass"

        for m in self.marks:
            self.total += m
            if m < 40:
                self.result = "Fail"

        self.percent = self.total / len(self.marks)

        if self.result == "Pass":
            if self.percent >= 80:
                self.grade = "First"
            elif self.percent >= 60:
                self.grade = "Second"
            else:
                self.grade = "Third"
        else:
            self.grade = "*"

    def displayMarksData(self):
        print("Roll number   :", self.roll)
        print("Student name  :", self.name)

        for i, m in enumerate(self.marks):
            if m < 40:
                print(f"Subject {i+1}     :{m} *")
            else:
                print(f"Subject {i+1}     :{m}")

        print("Total marks   :", self.total)
        print(f"Percentage    :{self.percent:.2f}%")
        print("Grade         :", self.grade)
        print("Result        :", self.result)


# Main program
name = "Rahul Tajne"
roll = 54
marks = [88, 99, 68, 78, 70, 90]

ms = MarksData()
ms.setMarksData(roll, name, marks)
ms.process()
ms.displayMarksData()
```

---

## ▶️ Example Output

```id="q2p7mz"
Roll number   : 54
Student name  : Rahul Tajne
Subject 1     :88
Subject 2     :99
Subject 3     :68
Subject 4     :78
Subject 5     :70
Subject 6     :90
Total marks   : 493
Percentage    : 82.17%
Grade         : First
Result        : Pass
```

---

## 📚 Concepts Used

* Class and Object
* Lists (array handling)
* Loops (`for`)
* Conditional statements (`if-else`)
* String formatting
* Basic grading logic

---

## 🎯 Use Case

This program helps beginners understand:

* Real-world student result processing
* How to handle lists in OOP
* Decision-making logic for grading systems

---

## 🔧 Future Improvements

* Take marks input from user
* Support multiple students (list of objects)
* Add subject names instead of numbers
* Export result to file (CSV or text)

---

## 📄 License

This project is open-source and free to use.
