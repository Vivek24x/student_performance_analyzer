# gui.py --- REAL SOFTWARE STYLE DASHBOARD

import tkinter as tk
import pandas as pd

from student import Student
from analyzer import Analyzer
from visualizer import Visualizer

# -------- LOAD DATA --------
data = pd.read_csv("data.csv")

students = []
for _, row in data.iterrows():
    students.append(Student(row["name"], row["maths"], row["science"], row["english"]))

analyzer = Analyzer(students)
viz = Visualizer(students)

# -------- MAIN WINDOW --------
root = tk.Tk()
root.title("Student Performance Software UI")
root.geometry("1000x600")
root.configure(bg="#12121c")

# -------- SIDEBAR --------
sidebar = tk.Frame(root, bg="#1e1e2f", width=200)
sidebar.pack(side="left", fill="y")

tk.Label(
    sidebar,
    text="🎓 Analyzer",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="white"
).pack(pady=20)

# -------- MAIN AREA --------
main = tk.Frame(root, bg="#12121c")
main.pack(side="right", fill="both", expand=True)

# -------- OUTPUT PANEL --------
output = tk.Text(
    main,
    bg="#1a1a2e",
    fg="white",
    font=("Arial", 11),
    height=10,
    bd=0
)
output.pack(fill="x", padx=20, pady=15)

def display(text):
    output.delete("1.0", tk.END)
    output.insert(tk.END, text)

# -------- LOGIC FUNCTIONS --------
def show_topper():
    t = analyzer.find_topper()
    display(f"🏆 Topper: {t.name}\nAverage: {t.get_average():.2f}")

def show_avg():
    avg = analyzer.class_average()
    display(f"📊 Class Average: {avg:.2f}")

def show_pass_fail():
    report = analyzer.pass_fail_report()
    display("\n".join([f"{n} - {s}" for n, s in report]))

def show_top5():
    top = analyzer.top_five()
    display("\n".join([f"{s.name} | {s.get_average():.2f}" for s in top]))

def show_graphs():
    viz.plot_averages()
    viz.plot_pass_fail()

# -------- CARD COMPONENT (REAL SOFTWARE STYLE) --------
def create_card(parent, title, command, color):

    card = tk.Frame(parent, bg=color, width=220, height=100)
    card.pack_propagate(False)

    label = tk.Label(
        card,
        text=title,
        font=("Arial", 13, "bold"),
        bg=color,
        fg="white"
    )
    label.pack(expand=True)

    # hover animation
    def enter(e):
        card.config(bg="#3a3a5a")
        label.config(bg="#3a3a5a")

    def leave(e):
        card.config(bg=color)
        label.config(bg=color)

    card.bind("<Enter>", enter)
    card.bind("<Leave>", leave)
    label.bind("<Enter>", enter)
    label.bind("<Leave>", leave)

    card.bind("<Button-1>", lambda e: command())
    label.bind("<Button-1>", lambda e: command())

    return card

# -------- DASHBOARD GRID --------
dashboard = tk.Frame(main, bg="#12121c")
dashboard.pack(pady=10)

create_card(dashboard, "🏆 Topper", show_topper, "#2e8bff").grid(row=0, column=0, padx=20, pady=15)
create_card(dashboard, "📊 Average", show_avg, "#ff7b00").grid(row=0, column=1, padx=20, pady=15)
create_card(dashboard, "✅ Pass/Fail", show_pass_fail, "#28a745").grid(row=1, column=0, padx=20, pady=15)
create_card(dashboard, "🥇 Top 5", show_top5, "#9c27b0").grid(row=1, column=1, padx=20, pady=15)
create_card(dashboard, "📈 Graphs", show_graphs, "#ff4d4d").grid(row=2, column=0, padx=20, pady=15)

# -------- SIDEBAR EXIT --------
tk.Button(
    sidebar,
    text="Exit",
    command=root.destroy,
    bg="#ff4d4d",
    fg="white",
    font=("Arial", 12, "bold"),
    width=12
).pack(side="bottom", pady=20)

root.mainloop()
