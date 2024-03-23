import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import pandas as pd
import os
import time
import datetime
import math

filepath = os.getcwd()
data_filepath = filepath + "\\dose_tracker_project\\dose_tracker_V1\\"

epoch_time = time.localtime()
current_time = time.ctime()
hm_time = time.strftime("%H:%M", epoch_time)

hour = time.strftime("%H", epoch_time)
minute = time.strftime("%M", epoch_time)
print(hour)
print(minute)

#this turns a structtime back into epoch time, don't know how tho
time.mktime


#experiment to figure out mktime
print(epoch_time)
print(current_time)
print(time.mktime(epoch_time))


print(current_time)


data = pd.read_csv(data_filepath + 'data.csv', index_col='medication')
med_list = list(data.index)

def run_func():
    data1['text']=name_var.get()

    #DEBUG PRINTS
    print(name_var.get())
    print(halflife_var.get())
    print(dose_var.get())
    print(hr_taken_var.get())
    print(min_taken_var.get())

def load_preset(var, indx, mode):
    value = name_var.get()
    if value in med_list:
        halflife_var.set(data.at[value, "half-life"])
        HL_unit_var.set(data.at[value, "HL_unit"])

window = tk.Tk()
window.title('Dose Tracker')
window.geometry('500x290')

name_var = tk.StringVar()
halflife_var = tk.StringVar()
HL_unit_var = tk.StringVar()
dose_var = tk.StringVar()
dose_unit_var = tk.StringVar()
hr_taken_var= tk.StringVar()
min_taken_var= tk.StringVar()


input_frame = ttk.LabelFrame(window, text='input')
input_frame.place(anchor='nw', relheight=1, relwidth=.3)
input_frame.rowconfigure(0, weight=1)
input_frame.rowconfigure(2, weight=1)
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(2, weight=1)

input_frame_frame = ttk.Frame(input_frame)
input_frame_frame.grid(row=0, column=1, sticky='n')

output_frame = ttk.LabelFrame(window, text='output')
output_frame.place(relx=0.3, y=0, relwidth = 0.7, relheight=1)

out_label_frame = ttk.Frame(output_frame)
out_label_frame.place(x=5, y=5, relwidth=0.4, relheight=0.5)

out_data_frame = ttk.Frame(output_frame)
out_data_frame.place(y=5, x=135, relwidth=0.5, relheight=0.5)
 
name_in_label = ttk.Label(input_frame_frame, text='Medication Name')
name_entry = ttk.Combobox(input_frame_frame, textvariable=name_var, width=18)
name_entry['values'] = med_list
halflife_label = ttk.Label(input_frame_frame, text='Half Life')
halflife_entry = ttk.Entry(input_frame_frame, textvariable=halflife_var, width=9)
HL_unit_label = ttk.Label(input_frame_frame, text='Unit')
HL_unit_entry = ttk.Combobox(input_frame_frame, textvariable=HL_unit_var, width=7)
HL_unit_entry['values'] = ('sec','min','hr')
dose_label = ttk.Label(input_frame_frame, text='Dose Taken')
dose_entry = ttk.Entry(input_frame_frame, textvariable=dose_var, width=9)
dose_unit_label = ttk.Label(input_frame_frame, text='Unit')
dose_unit_entry = ttk.Combobox(input_frame_frame, textvariable=dose_unit_var, width=7)
dose_unit_entry['values'] = ('mg','g')
time_taken_label = ttk.Label(input_frame_frame, text='Time Administered')


run_button = ttk.Button(input_frame_frame, text='Process', command=run_func, width=18)


time_frame = tk.Frame(input_frame_frame)

hr_taken_entry = ttk.Entry(time_frame, textvariable=hr_taken_var, width=2)
hr_taken_entry.insert(0, hour)
time_colon = ttk.Label(time_frame, text=":")
min_taken_entry = ttk.Entry(time_frame, textvariable=min_taken_var, width=2)
min_taken_entry.insert(0, minute)

hr_taken_entry.grid(row=0, column=0)
time_colon.grid(row=0, column=1)
min_taken_entry.grid(row=0, column=2)



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
time_frame.grid(row=7, column=0, columnspan=2)
run_button.grid(row=8, column=0, columnspan=2, pady=10)

name_var.trace_add('write', load_preset)

ttk.Label(out_label_frame, text='medication:').pack(anchor='nw')
ttk.Label(out_label_frame, text='blood concentration:').pack(anchor='nw')
ttk.Label(out_label_frame, text='time until cleared:').pack(anchor='nw')
ttk.Label(out_label_frame, text='secret fourth thing:').pack(anchor='nw')

data1 = ttk.Label(out_data_frame, text='')
data2 = ttk.Label(out_data_frame, text='')
data3 = ttk.Label(out_data_frame, text='')
data4 = ttk.Label(out_data_frame, text='')

data1.pack(anchor='nw')
data2.pack(anchor='nw')
data3.pack(anchor='nw')
data4.pack(anchor='nw')

window.mainloop()