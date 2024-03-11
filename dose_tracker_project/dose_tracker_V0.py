import tkinter as tk
from tkinter import ttk

def run_func():
    print(name_var.get())
    print(halflife_var.get())
    print(dose_var.get())
    print(time_taken_var.get())
    data1['text']=name_var.get()

window = tk.Tk()
window.title('Dose Tracker')
window.geometry('500x290')

name_var = tk.StringVar()
halflife_var = tk.StringVar()
dose_var = tk.StringVar()
time_taken_var= tk.StringVar()

input_frame = ttk.LabelFrame(window, text='input')
input_frame.place(anchor='nw', relheight=1)

output_frame = ttk.LabelFrame(window, text='output')
output_frame.place(relx=0.3, y=0, relwidth = 0.7, relheight=1)
 
name_in_label = ttk.Label(input_frame, text='Medication Name')
name_in_label.pack(side='top', anchor='nw', padx=15, pady=5)
name_entry = ttk.Entry(input_frame, textvariable=name_var)
name_entry.pack(side='top', anchor='nw', padx=15)

halflife_label = ttk.Label(input_frame, text='Half Life')
halflife_label.pack(side='top', anchor='nw', padx=15, pady=5)
halflife_entry = ttk.Entry(input_frame, textvariable=halflife_var)
halflife_entry.pack(side='top', anchor='nw', padx=15)

dose_label = ttk.Label(input_frame, text='Dose Taken')
dose_label.pack(side='top', anchor='nw', padx=15, pady=5)
dose_entry = ttk.Entry(input_frame, textvariable=dose_var)
dose_entry.pack(side='top', anchor='nw', padx=15)

time_taken_label = ttk.Label(input_frame, text='Time Administered')
time_taken_label.pack(side='top', anchor='nw', padx=15, pady=5)
time_taken_entry = ttk.Entry(input_frame, textvariable=time_taken_var)
time_taken_entry.pack(side='top', anchor='nw', padx=15)

out_label_frame = ttk.Frame(output_frame)
out_label_frame.place(x=5, y=5, relwidth=0.4, relheight=0.5)

out_data_frame = ttk.Frame(output_frame)
out_data_frame.place(y=5, x=135, relwidth=0.5, relheight=0.5)

ttk.Label(out_label_frame, text='medication:').pack(anchor='nw')
ttk.Label(out_label_frame, text='blood concentration:').pack(anchor='nw')
ttk.Label(out_label_frame, text='time until cleared').pack(anchor='nw')
ttk.Label(out_label_frame, text='secret fourth thing').pack(anchor='nw')

data1 = ttk.Label(out_data_frame, text='')
data2 = ttk.Label(out_data_frame, text='')
data3 = ttk.Label(out_data_frame, text='')
data4 = ttk.Label(out_data_frame, text='')

data1.pack(anchor='nw')
data2.pack(anchor='nw')
data3.pack(anchor='nw')
data4.pack(anchor='nw')



#ttk.Label(out_label_frame, background='red').pack(expand='true', fill='both')

run_button = ttk.Button(input_frame, text='Process', command=run_func)
run_button.pack(side='top', anchor='nw', padx=15, pady=23)

window.mainloop()