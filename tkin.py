# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 08:45:44 2019

@author: Sarvesh Angadi
"""

import tkinter as tk
from tkinter.simpledialog import askstring
root = tk.Tk()


root.withdraw()
a=[]
age = askstring("Age", "Enter your age")
a.append(age)
sex=askstring("Sex", "Enter your sex")
a.append(sex)
Diabetes=askstring("Diabetes", "Do you have diabetes?")
a.append(Diabetes)

import csv
spamWriter = csv.writer(open('H:/fuckx.csv', 'w'), delimiter=' ',
                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
spamWriter.writerow(['Spam'] * 5 + ['Baked Beans'])
spamWriter.writerow(a)



