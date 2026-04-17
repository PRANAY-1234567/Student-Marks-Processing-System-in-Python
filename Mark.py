class MarksData:
    
    def __init__(self):
        self.roll = 0
        self.Marks = []
        self.name = ""
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


# Main program (same as MarkList)
name = "Rahul Tajne"
roll = 54
marks = [88, 99, 68, 78, 70, 90]

ms = MarksData()
ms.setMarksData(roll, name, marks)
ms.process()
ms.displayMarksData()
