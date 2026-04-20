# Student Marks Analyzer ->

import numpy as np

print("Student Marks Analyzer📈\n")

n = int(input("Enter Number of Subjects: "))

Marks = np.array([int(input("Enter Marks Here: ")) for i in range(n)])

print("\nMarks Analysis📊 ->")

Avg = np.mean(Marks)
Max = np.max(Marks)
Min = np.min(Marks)

print(f"\nAverage of Marks: {round(Avg, 2)}\nHighest Marks: {Max}\nLowest Marks: {Min}")