import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Dose Tracker')
window.geometry('500x275')

def run_func():
    print(name_var.get())
    print(halflife_var.get())
    print(dose_var.get())
    print(time_taken_var.get())

name_var = tk.StringVar()
halflife_var = tk.StringVar()
dose_var = tk.StringVar()
time_taken_var= tk.StringVar()

name_label = ttk.Label(window, text='Medication Name')
name_label.pack(side='top', anchor='nw', padx=15, pady=5)
name_entry = ttk.Entry(window, textvariable=name_var)
name_entry.pack(side='top', anchor='nw', padx=15)

halflife_label = ttk.Label(window, text='Half Life')
halflife_label.pack(side='top', anchor='nw', padx=15, pady=5)
halflife_entry = ttk.Entry(window, textvariable=halflife_var)
halflife_entry.pack(side='top', anchor='nw', padx=15)

dose_label = ttk.Label(window, text='Dose Taken')
dose_label.pack(side='top', anchor='nw', padx=15, pady=5)
dose_entry = ttk.Entry(window, textvariable=dose_var)
dose_entry.pack(side='top', anchor='nw', padx=15)

time_taken_label = ttk.Label(window, text='Time Administered')
time_taken_label.pack(side='top', anchor='nw', padx=15, pady=5)
time_taken_entry = ttk.Entry(window, textvariable=time_taken_var)
time_taken_entry.pack(side='top', anchor='nw', padx=15)

run_button = ttk.Button(window, text='Process', command=run_func)
run_button.pack(side='top', anchor='nw', padx=15, pady=23)

window.mainloop()