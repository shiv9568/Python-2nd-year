import tkinter as tk
from tkinter import ttk
import pandas as pd

def load_data(file_path):
    
    medical_data = pd.read_csv(file_path)
    return medical_data

def display_data():
    
    root = tk.Tk()
    root.title("Medical Diagnosis Dataset")

    
    file_path = "healthcare_dataset.csv"  
    medical_data = load_data(file_path)

    
    tree = ttk.Treeview(root)
    tree["columns"] = tuple(medical_data.columns)
    tree["show"] = "headings"
    
    
    for column in medical_data.columns:
        tree.heading(column, text=column)

  
    for index, row in medical_data.iterrows():
        tree.insert("", "end", values=tuple(row))

    
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    
    tree.pack(expand=True, fill="both")

    
    root.mainloop()


display_data()
