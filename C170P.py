import tkinter as tk
root = tk.Tk()
root.title("Grade Percentage Calculator")
root.geometry("500x500")

class Grade3:
    def __init__(self, language_arts, mathematics):
        self.language_arts = language_arts
        self.mathematics = mathematics

    def percentage(self):
        total_marks = self.language_arts + self.mathematics
        total_marks_with_100 = total_marks * 100
        grade_3_percentage = total_marks_with_100 / 200
        percentage_grade_3_label.config(text=f"Grade 3 Percentage: {grade_3_percentage}%")

class Grade5:
    def __init__(self, language_arts, mathematics, social_studies):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies

    def percentage(self):
        total_marks = self.language_arts + self.mathematics + self.social_studies
        total_marks_with_100 = total_marks * 100
        grade_5_percentage = total_marks_with_100 / 300
        percentage_grade_5_label.config(text=f"Grade 5 Percentage: {grade_5_percentage}%")

class Grade10:
    def __init__(self, language_arts, mathematics, social_studies, foreign_language):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
        self.foreign_language = foreign_language

    def percentage(self):
        total_marks = self.language_arts + self.mathematics + self.social_studies + self.foreign_language
        total_marks_with_100 = total_marks * 100
        grade_10_percentage = total_marks_with_100 / 400
        percentage_grade_10_label.config(text=f"Grade 10 Percentage: {grade_10_percentage}%")

# Create the main window


# Create labels
percentage_grade_3_label = tk.Label(root, text="Grade 3 Percentage: ", padx=10, pady=10)
percentage_grade_5_label = tk.Label(root, text="Grade 5 Percentage: ", padx=10, pady=10)
percentage_grade_10_label = tk.Label(root, text="Grade 10 Percentage: ", padx=10, pady=10)

# Create objects for grades
object_grade_3 = Grade3(85, 90)
object_grade_5 = Grade5(80, 85, 90)
object_grade_10 = Grade10(75, 80, 85, 90)

# Create buttons for grades
button_grade_3 = tk.Button(root, text="Grade 3", command=object_grade_3.percentage, padx=10, pady=10)
button_grade_5 = tk.Button(root, text="Grade 5", command=object_grade_5.percentage, padx=10, pady=10)
button_grade_10 = tk.Button(root, text="Grade 10", command=object_grade_10.percentage, padx=10, pady=10)

# Place labels and buttons on the root window
percentage_grade_3_label.pack()
button_grade_3.pack()
percentage_grade_5_label.pack()
button_grade_5.pack()
percentage_grade_10_label.pack()
button_grade_10.pack()

# Run the Tkinter event loop
root.mainloop()
