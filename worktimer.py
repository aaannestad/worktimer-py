from tkinter import *
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
        'clockedin?': False,
        'time': 30
    }
}

def makebutton():
    row = 1
    for item in data['projects']:
        ttk.Button(frm, text=data['projects'][item]['name']).grid(column=0,row=row)
        ttk.Label(frm, text=data['projects'][item]['starttime']).grid(column=1, row=row)
        row = row + 1

root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text=data['clock']['time']).grid(column=0, row=0, columnspan=2)

makebutton()

root.mainloop()