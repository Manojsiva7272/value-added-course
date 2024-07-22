
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import pandas as pd

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")

        self.num_students = 0
        self.students_data = []

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Enter Number of Students:")
        self.label.pack(pady=10)
        
        self.num_students_entry = tk.Entry(self.root)
        self.num_students_entry.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_num_students)
        self.submit_button.pack(pady=10)

    def submit_num_students(self):
        try:
            self.num_students = int(self.num_students_entry.get())
            self.students_data = []
            self.num_students_entry.delete(0, tk.END)

            self.label.config(text=f"Enter details for {self.num_students} students")
            self.create_student_entries()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")

    def create_student_entries(self):
        self.entries = []

        for i in range(self.num_students):
            student_frame = tk.Frame(self.root)
            student_frame.pack(pady=5)

            reg_label = tk.Label(student_frame, text=f"Student {i+1} Register Number:")
            reg_label.grid(row=0, column=0)
            reg_entry = tk.Entry(student_frame)
            reg_entry.grid(row=0, column=1)

            name_label = tk.Label(student_frame, text="Name:")
            name_label.grid(row=0, column=2)
            name_entry = tk.Entry(student_frame)
            name_entry.grid(row=0, column=3)

            mark1_label = tk.Label(student_frame, text="Mark 1:")
            mark1_label.grid(row=0, column=4)
            mark1_entry = tk.Entry(student_frame)
            mark1_entry.grid(row=0, column=5)

            mark2_label = tk.Label(student_frame, text="Mark 2:")
            mark2_label.grid(row=0, column=6)
            mark2_entry = tk.Entry(student_frame)
            mark2_entry.grid(row=0, column=7)

            mark3_label = tk.Label(student_frame, text="Mark 3:")
            mark3_label.grid(row=0, column=8)
            mark3_entry = tk.Entry(student_frame)
            mark3_entry.grid(row=0, column=9)

            self.entries.append((reg_entry, name_entry, mark1_entry, mark2_entry, mark3_entry))

        self.save_button = tk.Button(self.root, text="Save", command=self.save_student_data)
        self.save_button.pack(pady=10)

    def save_student_data(self):
        for entry in self.entries:
            reg = entry[0].get()
            name = entry[1].get()
            mark1 = entry[2].get()
            mark2 = entry[3].get()
            mark3 = entry[4].get()

            if not (reg and name and mark1 and mark2 and mark3):
                messagebox.showerror("Invalid Input", "Please fill all fields")
                return

            try:
                mark1 = float(mark1)
                mark2 = float(mark2)
                mark3 = float(mark3)
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid marks")
                return

            self.students_data.append((reg, name, mark1, mark2, mark3))

        self.display_graph()

    def display_graph(self):
        df = pd.DataFrame(self.students_data, columns=["Register Number", "Name", "Mark 1", "Mark 2", "Mark 3"])

        df.plot(x="Name", y=["Mark 1", "Mark 2", "Mark 3"], kind="bar")
        plt.title("Student Marks")
        plt.ylabel("Marks")
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
