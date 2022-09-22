from tkinter import *
import tkinter
from tkinter import ttk

import pickle

data = {
    'projects': {
      'project': {
           'name': 'Project',
           'starttime': 0
    },
       'another': {
           'name': 'Another',
           'starttime': 0
       }
    },
    'clock': {
        'clockedin?': FALSE,
        'time': 30
    }
}

root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text=data['clock']['time']).pack()

for item in data['projects']:
    ttk.Button(frm, text=data['projects'][item]['name']).pack(side=tkinter.LEFT)

root.mainloop()