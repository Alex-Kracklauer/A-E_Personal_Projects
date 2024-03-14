import tkinter as tk
from tkinter import ttk
#import ttkbootstrap as ttk
import time
import math

current_time = time.strftime('%H:%M')
print(current_time)

def run_func():
    data1['text']=name_var.get()

    #debug bs
    print(name_var.get())
    print(halflife_var.get())
    print(dose_var.get())
    print(time_taken_var.get())

window = tk.Tk()
window.title('Dose Tracker')
window.geometry('500x290')

name_var = tk.StringVar()
halflife_var = tk.StringVar()
HL_unit_var = tk.StringVar()
dose_var = tk.StringVar()
dose_unit_var = tk.StringVar()
time_taken_var= tk.StringVar()

input_frame = ttk.LabelFrame(window, text='input')
input_frame.place(anchor='nw', relheight=1, relwidth=.3)

output_frame = ttk.LabelFrame(window, text='output')
output_frame.place(relx=0.3, y=0, relwidth = 0.7, relheight=1)
 
name_in_label = ttk.Label(input_frame, text='Medication Name')

name_entry = ttk.Combobox(input_frame, textvariable=name_var, width=17)
name_entry['values'] = ('Adderall','Caffiene','Third Thing')

halflife_label = ttk.Label(input_frame, text='Half Life')
halflife_entry = ttk.Entry(input_frame, textvariable=halflife_var, width=9)
HL_unit_label = ttk.Label(input_frame, text='Unit')
HL_unit_entry = ttk.Combobox(input_frame, textvariable=HL_unit_var, width=7)
dose_label = ttk.Label(input_frame, text='Dose Taken')
dose_entry = ttk.Entry(input_frame, textvariable=dose_var, width=9)
dose_unit_label = ttk.Label(input_frame, text='Unit')
dose_unit_entry = ttk.Combobox(input_frame, textvariable=dose_unit_var, width=7)
time_taken_label = ttk.Label(input_frame, text='Time Administered')
time_taken_entry = ttk.Entry(input_frame, textvariable=time_taken_var, width=20)
time_taken_entry.insert(0, current_time)

run_button = ttk.Button(input_frame, text='Process', command=run_func)

''
name_in_label.grid(row=0, column=0, columnspan=2)
name_entry.grid(row=1, column=0, columnspan=2)
halflife_label.grid(row=2, column=0)
halflife_entry.grid(row=3, column=0)
HL_unit_label.grid(row=2, column=1)
HL_unit_entry.grid(row=3, column=1)
dose_label.grid(row=4, column=0)
dose_entry.grid(row=5, column=0)
dose_unit_label.grid(row=4, column=1)
dose_unit_entry.grid(row=5, column=1)
time_taken_label.grid(row=6, column=0, columnspan=2)
time_taken_entry.grid(row=7, column=0, columnspan=2)
run_button.grid(row=8, column=0, columnspan=2)
''
'''
name_in_label.pack(side='top', anchor='nw', padx=15, pady=5)
name_entry.pack(side='top', anchor='nw', padx=15)
halflife_label.pack(side='top', anchor='nw', padx=15, pady=5)
halflife_entry.pack(side='top', anchor='nw', padx=15)
dose_label.pack(side='top', anchor='nw', padx=15, pady=5)
dose_entry.pack(side='top', anchor='nw', padx=15)
time_taken_label.pack(side='top', anchor='nw', padx=15, pady=5)
time_taken_entry.pack(side='top', anchor='nw', padx=15)
run_button.pack(side='top', anchor='nw', padx=15, pady=23)
'''

out_label_frame = ttk.Frame(output_frame)
out_label_frame.place(x=5, y=5, relwidth=0.4, relheight=0.5)

out_data_frame = ttk.Frame(output_frame)
out_data_frame.place(y=5, x=135, relwidth=0.5, relheight=0.5)

ttk.Label(out_label_frame, text='medication:').pack(anchor='nw')
ttk.Label(out_label_frame, text='blood concentration:').pack(anchor='nw')
ttk.Label(out_label_frame, text='time until cleared:').pack(anchor='nw')
ttk.Label(out_label_frame, text='secret fourth thing:').pack(anchor='nw')

#data1 = ttk.Label(out_data_frame, textvariable=name_var)
data1 = ttk.Label(out_data_frame, text='')
data2 = ttk.Label(out_data_frame, text='')
data3 = ttk.Label(out_data_frame, text='')
data4 = ttk.Label(out_data_frame, text='')

data1.pack(anchor='nw')
data2.pack(anchor='nw')
data3.pack(anchor='nw')
data4.pack(anchor='nw')

#ttk.Label(out_label_frame, background='red').pack(expand='true', fill='both')

window.mainloop()