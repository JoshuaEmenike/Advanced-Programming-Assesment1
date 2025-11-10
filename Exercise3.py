import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

#  File Handling 
def load_students(filename="Marks.txt"):
    students = []
    try:
        with open(filename, "r") as file:
            lines = [line.strip() for line in file if line.strip()]
            for line in lines[1:]:
                parts = [x.strip() for x in line.split(",")]
                if len(parts) == 6:
                    students.append({
                        "code": int(parts[0]),
                        "name": parts[1],
                        "coursework": list(map(int, parts[2:5])),
                        "exam": int(parts[5])
                    })
    except FileNotFoundError:
        messagebox.showerror("Error", "Marks.txt file not found!")
    return students

def save_students(students, filename="Marks.txt"):
    try:
        with open(filename, "w") as file:
            file.write("Code,Name,Coursework1,Coursework2,Coursework3,Exam\n")
            for s in students:
                file.write(f"{s['code']},{s['name']},{s['coursework'][0]},{s['coursework'][1]},{s['coursework'][2]},{s['exam']}\n")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Could not save file: {e}")
        return False

def calc_total(student):
    return sum(student['coursework']) + student['exam']

def calc_percentage(student):
    return round(calc_total(student) / 160 * 100, 2)

def calc_grade(percentage):
    if percentage >= 70: return "A"
    elif percentage >= 60: return "B"
    elif percentage >= 50: return "C"
    elif percentage >= 40: return "D"
    else: return "F"

#  GUI Application 
class StudentManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Manager")
        self.root.geometry("900x600")
        self.root.configure(bg="#d9e3e8")
        self.students = load_students()

        # Title Label
        tk.Label(root, text="Student Manager", font=("Arial", 24, "bold"), bg="#d9e3e8").pack(pady=15)

        # Button Frame - Top Row
        btn_frame_top = tk.Frame(root, bg="#d9e3e8")
        btn_frame_top.pack(pady=5)

        self.btn_all = tk.Button(btn_frame_top, text="View All Students", command=self.view_all,
                                 width=18, font=("Arial", 11), relief="raised", bg="#ffffff", bd=2)
        self.btn_highest = tk.Button(btn_frame_top, text="Highest", command=self.show_highest,
                                     width=12, font=("Arial", 11), relief="raised", bg="#ffffff", bd=2)
        self.btn_lowest = tk.Button(btn_frame_top, text="Lowest", command=self.show_lowest,
                                    width=12, font=("Arial", 11), relief="raised", bg="#ffffff", bd=2)
        self.btn_sort = tk.Button(btn_frame_top, text="Sort", command=self.sort_students,
                                  width=12, font=("Arial", 11), relief="raised", bg="#ffffff", bd=2)

        self.btn_all.grid(row=0, column=0, padx=8, pady=5)
        self.btn_highest.grid(row=0, column=1, padx=8, pady=5)
        self.btn_lowest.grid(row=0, column=2, padx=8, pady=5)
        self.btn_sort.grid(row=0, column=3, padx=8, pady=5)

        # Button Frame - Bottom Row
        btn_frame_bottom = tk.Frame(root, bg="#d9e3e8")
        btn_frame_bottom.pack(pady=5)

        self.btn_add = tk.Button(btn_frame_bottom, text="Add", command=self.add_student,
                                width=12, font=("Arial", 11), relief="raised", bg="#ffffff", bd=2)
        self.btn_delete = tk.Button(btn_frame_bottom, text="Delete", command=self.delete_student,
                                    width=12, font=("Arial", 11), relief="raised", bg="#ffffff", bd=2)
        self.btn_update = tk.Button(btn_frame_bottom, text="Update", command=self.update_student,
                                    width=12, font=("Arial", 11), relief="raised", bg="#ffffff", bd=2)

        self.btn_add.grid(row=0, column=0, padx=8, pady=5)
        self.btn_delete.grid(row=0, column=1, padx=8, pady=5)
        self.btn_update.grid(row=0, column=2, padx=8, pady=5)

        # Individual View Frame
        indiv_frame = tk.Frame(root, bg="#d9e3e8")
        indiv_frame.pack(pady=15)

        tk.Label(indiv_frame, text="View Individual Student Record:", font=("Arial", 12), bg="#d9e3e8").grid(row=0, column=0, padx=10)
        self.selected_name = tk.StringVar()
        self.combo = ttk.Combobox(indiv_frame, textvariable=self.selected_name, width=25, state="readonly", font=("Arial", 11))
        self.combo.grid(row=0, column=1, padx=10)
        self.update_combo()
        self.btn_view = tk.Button(indiv_frame, text="View", command=self.view_individual,
                                  width=10, font=("Arial", 11), relief="raised", bg="#ffffff", bd=2)
        self.btn_view.grid(row=0, column=2, padx=10)

        # Output Area
        output_frame = tk.Frame(root, bg="#d9e3e8")
        output_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        self.output = tk.Text(output_frame, width=90, height=18, wrap="word", font=("Consolas", 10), bg="#ffffff", relief="solid", bd=1)
        scrollbar = tk.Scrollbar(output_frame, command=self.output.yview)
        self.output.config(yscrollcommand=scrollbar.set)
        
        self.output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.output.config(state="disabled")

    #  Helper Methods 
    def update_combo(self):
        self.combo["values"] = [s["name"] for s in self.students]
        if self.students:
            self.combo.current(0)

    def display_students(self, data):
        self.output.config(state="normal")
        self.output.delete(1.0, tk.END)
        for s in data:
            total = sum(s['coursework'])
            percent = calc_percentage(s)
            grade = calc_grade(percent)
            self.output.insert(tk.END, f"Name: {s['name']}\n")
            self.output.insert(tk.END, f"Number: {s['code']}\n")
            self.output.insert(tk.END, f"Coursework Total: {total}\n")
            self.output.insert(tk.END, f"Exam Mark: {s['exam']}\n")
            self.output.insert(tk.END, f"Overall Percentage: {percent:.2f}%\n")
            self.output.insert(tk.END, f"Grade: {grade}\n")
            self.output.insert(tk.END, "-" * 60 + "\n\n")
        self.output.config(state="disabled")

    #  View Functions 
    def view_all(self):
        if not self.students:
            messagebox.showinfo("Info", "No students to display.")
            return
        self.display_students(self.students)

    def view_individual(self):
        name = self.selected_name.get()
        if not name:
            messagebox.showinfo("Info", "Please select a student.")
            return
        for s in self.students:
            if s["name"] == name:
                self.display_students([s])
                return
        messagebox.showerror("Error", "Student not found!")

    def show_highest(self):
        if not self.students:
            messagebox.showinfo("Info", "No students to display.")
            return
        best = max(self.students, key=lambda s: calc_total(s))
        self.display_students([best])

    def show_lowest(self):
        if not self.students:
            messagebox.showinfo("Info", "No students to display.")
            return
        worst = min(self.students, key=lambda s: calc_total(s))
        self.display_students([worst])

    def sort_students(self):
        if not self.students:
            messagebox.showinfo("Info", "No students to sort.")
            return
        self.students.sort(key=lambda s: calc_total(s), reverse=True)
        self.update_combo()
        self.display_students(self.students)
        messagebox.showinfo("Success", "Students sorted by total marks (highest to lowest).")

    # ========== CRUD Functions ==========
    def add_student(self):
        dialog = AddStudentDialog(self.root)
        self.root.wait_window(dialog.dialog)
        
        if dialog.result:
            self.students.append(dialog.result)
            save_students(self.students)
            self.update_combo()
            messagebox.showinfo("Success", f"Student {dialog.result['name']} added successfully!")

    def delete_student(self):
        name = self.selected_name.get()
        if not name:
            messagebox.showinfo("Info", "Please select a student to delete.")
            return
        
        response = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {name}?")
        if response:
            self.students = [s for s in self.students if s["name"] != name]
            save_students(self.students)
            self.update_combo()
            self.output.config(state="normal")
            self.output.delete(1.0, tk.END)
            self.output.config(state="disabled")
            messagebox.showinfo("Success", f"Student {name} deleted successfully!")

    def update_student(self):
        name = self.selected_name.get()
        if not name:
            messagebox.showinfo("Info", "Please select a student to update.")
            return
        
        student = next((s for s in self.students if s["name"] == name), None)
        if not student:
            messagebox.showerror("Error", "Student not found!")
            return
        
        dialog = UpdateStudentDialog(self.root, student)
        self.root.wait_window(dialog.dialog)
        
        if dialog.result:
            idx = self.students.index(student)
            self.students[idx] = dialog.result
            save_students(self.students)
            self.update_combo()
            messagebox.showinfo("Success", f"Student {dialog.result['name']} updated successfully!")

#  Dialog Classes 
class AddStudentDialog:
    def __init__(self, parent):
        self.result = None
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Add Student")
        self.dialog.geometry("400x350")
        self.dialog.configure(bg="#e8f0f2")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        tk.Label(self.dialog, text="Add New Student", font=("Arial", 14, "bold"), bg="#e8f0f2").pack(pady=10)
        
        frame = tk.Frame(self.dialog, bg="#e8f0f2")
        frame.pack(pady=10, padx=20)
        
        tk.Label(frame, text="Student Code:", bg="#e8f0f2").grid(row=0, column=0, sticky="w", pady=5)
        self.code_entry = tk.Entry(frame, width=25)
        self.code_entry.grid(row=0, column=1, pady=5, padx=5)
        
        tk.Label(frame, text="Name:", bg="#e8f0f2").grid(row=1, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(frame, width=25)
        self.name_entry.grid(row=1, column=1, pady=5, padx=5)
        
        tk.Label(frame, text="Coursework 1:", bg="#e8f0f2").grid(row=2, column=0, sticky="w", pady=5)
        self.cw1_entry = tk.Entry(frame, width=25)
        self.cw1_entry.grid(row=2, column=1, pady=5, padx=5)
        
        tk.Label(frame, text="Coursework 2:", bg="#e8f0f2").grid(row=3, column=0, sticky="w", pady=5)
        self.cw2_entry = tk.Entry(frame, width=25)
        self.cw2_entry.grid(row=3, column=1, pady=5, padx=5)
        
        tk.Label(frame, text="Coursework 3:", bg="#e8f0f2").grid(row=4, column=0, sticky="w", pady=5)
        self.cw3_entry = tk.Entry(frame, width=25)
        self.cw3_entry.grid(row=4, column=1, pady=5, padx=5)
        
        tk.Label(frame, text="Exam Mark:", bg="#e8f0f2").grid(row=5, column=0, sticky="w", pady=5)
        self.exam_entry = tk.Entry(frame, width=25)
        self.exam_entry.grid(row=5, column=1, pady=5, padx=5)
        
        btn_frame = tk.Frame(self.dialog, bg="#e8f0f2")
        btn_frame.pack(pady=15)
        
        tk.Button(btn_frame, text="Add", command=self.add, width=10, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Cancel", command=self.dialog.destroy, width=10).grid(row=0, column=1, padx=5)
    
    def add(self):
        try:
            code = int(self.code_entry.get())
            name = self.name_entry.get().strip()
            cw1 = int(self.cw1_entry.get())
            cw2 = int(self.cw2_entry.get())
            cw3 = int(self.cw3_entry.get())
            exam = int(self.exam_entry.get())
            
            if not name:
                messagebox.showerror("Error", "Name cannot be empty!")
                return
            
            self.result = {
                "code": code,
                "name": name,
                "coursework": [cw1, cw2, cw3],
                "exam": exam
            }
            self.dialog.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for marks and code!")

class UpdateStudentDialog:
    def __init__(self, parent, student):
        self.result = None
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Update Student")
        self.dialog.geometry("400x350")
        self.dialog.configure(bg="#e8f0f2")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        tk.Label(self.dialog, text="Update Student", font=("Arial", 14, "bold"), bg="#e8f0f2").pack(pady=10)
        
        frame = tk.Frame(self.dialog, bg="#e8f0f2")
        frame.pack(pady=10, padx=20)
        
        tk.Label(frame, text="Student Code:", bg="#e8f0f2").grid(row=0, column=0, sticky="w", pady=5)
        self.code_entry = tk.Entry(frame, width=25)
        self.code_entry.insert(0, str(student["code"]))
        self.code_entry.grid(row=0, column=1, pady=5, padx=5)
        
        tk.Label(frame, text="Name:", bg="#e8f0f2").grid(row=1, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(frame, width=25)
        self.name_entry.insert(0, student["name"])
        self.name_entry.grid(row=1, column=1, pady=5, padx=5)
        
        tk.Label(frame, text="Coursework 1:", bg="#e8f0f2").grid(row=2, column=0, sticky="w", pady=5)
        self.cw1_entry = tk.Entry(frame, width=25)
        self.cw1_entry.insert(0, str(student["coursework"][0]))
        self.cw1_entry.grid(row=2, column=1, pady=5, padx=5)
        
        tk.Label(frame, text="Coursework 2:", bg="#e8f0f2").grid(row=3, column=0, sticky="w", pady=5)
        self.cw2_entry = tk.Entry(frame, width=25)
        self.cw2_entry.insert(0, str(student["coursework"][1]))
        self.cw2_entry.grid(row=3, column=1, pady=5, padx=5)
        
        tk.Label(frame, text="Coursework 3:", bg="#e8f0f2").grid(row=4, column=0, sticky="w", pady=5)
        self.cw3_entry = tk.Entry(frame, width=25)
        self.cw3_entry.insert(0, str(student["coursework"][2]))
        self.cw3_entry.grid(row=4, column=1, pady=5, padx=5)
        
        tk.Label(frame, text="Exam Mark:", bg="#e8f0f2").grid(row=5, column=0, sticky="w", pady=5)
        self.exam_entry = tk.Entry(frame, width=25)
        self.exam_entry.insert(0, str(student["exam"]))
        self.exam_entry.grid(row=5, column=1, pady=5, padx=5)
        
        btn_frame = tk.Frame(self.dialog, bg="#e8f0f2")
        btn_frame.pack(pady=15)
        
        tk.Button(btn_frame, text="Update", command=self.update, width=10, bg="#2196F3", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Cancel", command=self.dialog.destroy, width=10).grid(row=0, column=1, padx=5)
    
    def update(self):
        try:
            code = int(self.code_entry.get())
            name = self.name_entry.get().strip()
            cw1 = int(self.cw1_entry.get())
            cw2 = int(self.cw2_entry.get())
            cw3 = int(self.cw3_entry.get())
            exam = int(self.exam_entry.get())
            
            if not name:
                messagebox.showerror("Error", "Name cannot be empty!")
                return
            
            self.result = {
                "code": code,
                "name": name,
                "coursework": [cw1, cw2, cw3],
                "exam": exam
            }
            self.dialog.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for marks and code!")

# ========== Run App ==========
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagerApp(root)
    root.mainloop()