import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import pandas as pd
import os
import time
from datetime import datetime, timedelta
import math

#window setup
window = tk.Tk()
window.title('Dose Tracker')
window.geometry('500x290')

#tkinter variables
name_var = tk.StringVar()
halflife_var = tk.StringVar()
HL_unit_var = tk.StringVar()
dose_var = tk.StringVar()
dose_unit_var = tk.StringVar()
hr_taken_var= tk.StringVar()
min_taken_var= tk.StringVar()

#filepath lookup to locate data files
filepath = os.getcwd()
data_filepath = filepath + "\\dose_tracker_project\\dose_tracker_V1\\"
data = pd.read_csv(data_filepath + 'data.csv', index_col='medication')
med_list = list(data.index)

#global time functions
current_time = time.localtime()
#print(current_time)
hour = time.strftime("%H", current_time)
minute = time.strftime("%M", current_time)
ep_time_taken = (time.mktime(time.localtime()))

def process_time():
    #pull data to insert to string
    hr_input = hr_taken_var.get()
    min_input = min_taken_var.get()

    #generate time string with writable variables
    date = time.strftime("%m/%d/%Y", current_time)
    raw_time = date+','+' '+hr_input+":"+min_input+":"+time.strftime("%S", current_time)
    #print(raw_time)

    #reformat edited time into struct_time standard
    output_time = time.strptime(raw_time, "%m/%d/%Y, %H:%M:%S")
    #print(output_time)

    #generate time administered in epoch format for save data
    ep_time_taken = time.mktime(output_time)

    #print(ep_time_taken)

    #function output
    return output_time

#proceses user input and generate output data
def run_func():
    data1['text']=name_var.get()
    data4['text']=process_time()
    
    #output variable bank
    class med:
        name = name_var.get()
        half = halflife_var.get()
        dose = dose_var
        time = time.mktime(process_time())
    print(med)

#pull medication data from the preset file
def load_preset(var, indx, mode):
    value = name_var.get()
    if value in med_list:
        halflife_var.set(data.at[value, "half-life"])
        HL_unit_var.set(data.at[value, "HL_unit"])
        dose_unit_var.set(data.at[value, "dose_unit"])


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