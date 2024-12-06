import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import joblib

def predict_data():
    file_path = filedialog.askopenfilename(title="Select prediction data file", filetypes=(("CSV files", "*.csv"),))
    data = pd.read_csv(file_path,header=None)
    knn_model = joblib.load('r_vs_m_model')
    predictions = knn_model.predict(data)
    print(predictions)
    if predictions == 'M':
        s = "Mine"
    else:
        s= "Rock"
    messagebox.showinfo(title="Predictions", message=str(s))

window = tk.Tk()
window.geometry("900x700")
window.configure(bg="black")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window.winfo_reqwidth()) / 2
y = (screen_height - window.winfo_reqheight()) / 2
window.geometry("+%d+%d" % (x, y))

label = tk.Label(window, text="ROCK vs MINE", font=("Impact", 40),fg="white",bd=5,bg="black")
label.pack(pady=(100, 5))

button = tk.Button(window, text="Select The Data File",font=("Times New Roman", 26), command=predict_data)
button.pack()
button_width = 150
button_height = 30
button_x = (300 - button_width) / 2
button_y = (100 - button_height) / 2
button.place(relx=button_x/300, rely=button_y/100, relwidth=button_width/300, relheight=button_height/100)

label = tk.Label(window, text="Project", font=("Impact", 40),fg="white",bd=5,bg="black")
label.pack(pady=(350, 5))

window.mainloop()
