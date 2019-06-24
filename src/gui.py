#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:53:02 2019

@author: DannySwift
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import *


class gui:
    def __init__(self):
        self.top = tk.Tk()
        self.input_button = tk.Button(self.top, text='Set Input', width=25, 
                                      command=self.set_input)
        self.input_button.grid(row=0, column=0)
        self.output_button = tk.Button(self.top, text='Set Output', width = 25,
                                       command=self.set_output)
        self.output_button.grid(row=0, column=1)
        self.run_button = tk.Button(self.top, text='Run', 
                                    width=25, command=self.run)
        self.run_button.grid(row=1)
        self.add_button = tk.Button(self.top, text='Add Tag', 
                                    width=25, command=self.add_tag)
        self.add_button.grid(row=2)
        self.tags = []
        self.values = []
        self.rows = 3
        self.top.mainloop()
    
    
    def add_tag(self):
        tk.Label(self.top, text='Tag').grid(row=self.rows)
        tag = tk.Entry(self.top)
        tag.grid(row=self.rows, column=1)
        self.tags.append(tag)
        tk.Label(self.top, text='Value').grid(row=self.rows, column=2)
        value = tk.Entry(self.top)
        value.grid(row=self.rows, column=3)
        self.values.append(value)
        self.rows += 1
        self.top.mainloop()
    
    
    def set_input(self):
        self.top.input = filedialog.askdirectory()
        
    
    def set_output(self):
        self.top.output = filedialog.askdirectory()
        
    
    def run(self):
        print(self.top.input)