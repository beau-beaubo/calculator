"""UI"""

import tkinter as tk
from tkinter import ttk
from keypad import Keypad
from control import CalculatorControl


class CalculatorUI(tk.Tk):
    """Keypad"""
    def __init__(self):
        # keynames and columns
        super().__init__()
        self.control = CalculatorControl()
        self.init_components()

    def init_components(self) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        """
        self.frame1 = Keypad(self, list('789456123 0.'), 3)
        self.math_frame = Keypad(self, ['(', ')', '**', 'sqrt', 'log', 'log10', 'log2', 'exp', 'CLR', 'DEL'], 5)
        self.frame2 = Keypad(self, ['*', '/', '+', '-', '^', '%', '='])
        self.text = tk.StringVar()
        self.title('Calculator')
        self.label = tk.Label(self, width=20, height=2, foreground='pink', anchor="e", font=('Monospace', 14))
        self.history_box = ttk.Combobox(self, width=10, height=10, state="readonly")
        self.history_box.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.label.pack(side=tk.TOP, expand=False, fill=tk.BOTH)
        self.label.configure(background='Black')
        self.math_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.math_frame.configure(foreground='Black', background='Pink', font=('Monospace', 10))
        self.frame1.configure(foreground='Black', background='Pink', font=('Monospace', 10))
        self.frame1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.frame1.bind('<Button>', self.handle_click)
        self.frame2.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        self.frame2.configure(foreground='Black', background='Pink', font=('Monospace', 10))
        self.frame2.bind('<Button>', self.handle_click)
        self.math_frame.bind('<Button>', self.handle_click)

    def handle_click(self, event):
        """Handle click"""
        math_func = ['sqrt', 'log', 'log10', 'log2', 'exp']
        text = event.widget['text']
        if text == 'DEL':
            self.control.delete_last_char()
        elif text == 'CLR':
            self.control.clear_display()
        elif text in math_func:
            self.handle_math_functions(text)
        elif text == '=':
            if self.control.is_valid_expression():
                self.label.configure(background='Black')
                equation = self.control.get_display()
                result = self.control.evaluate_display()
                self.control.add_to_history(equation, result)
            else:
                self.control.raise_error()
                self.label.configure(background='Red')
                self.update_display()
        else:
            self.control.add_to_display(text)
        self.update_display()
        self.update_history()

    def handle_math_functions(self, function_name):
        """Handle math function buttons"""
        display = self.control.get_display()
        if display.endswith(('+', '-', '*', '/')):
            self.control.add_to_display(function_name + '(')
        else:
            self.control.add_to_display(function_name + '(')
        self.update_display()

    def update_display(self):
        """Update the display label"""
        self.text.set(self.control.get_display())
        self.label.config(text=self.text.get())

    def update_history(self):
        """Update the history box with the latest calculations"""
        self.history_box['values'] = self.control.get_history()

    def run(self):
        """Run UI"""
        self.mainloop()

    def make_keypad(self) -> tk.Frame:
        """Create a frame containing buttons for the numeric keys."""
        c = 0
        _list = []
        for i in self.keynames:
            _list.append(tk.Button(self.frame1, text=i))
        for row in range(4):
            for col in range(3):
                _list[c].grid(column=col, row=row, sticky=tk.NSEW, padx=2, pady=2)
                c += 1
        self.frame1.rowconfigure(0, weight=5)
        self.frame1.rowconfigure(1, weight=5)
        self.frame1.rowconfigure(2, weight=5)
        self.frame1.rowconfigure(3, weight=5)
        self.frame1.columnconfigure(0, weight=5)
        self.frame1.columnconfigure(1, weight=5)
        self.frame1.columnconfigure(2, weight=5)
        return self.frame1

    def make_operators_pad(self) -> tk.Frame:
        """Create a frame containing buttons for the numeric keys."""
        operator = ['*', '/', '+', '-', '^', '=']
        operator_button = []
        for operators in operator:
            operator_button.append(tk.Button(self.frame2, text=operators))
        c = 0
        for row in range(6):
            operator_button[c].grid(column=4, row=row, sticky=tk.NSEW, pady=2)
            c += 1
        self.frame2.rowconfigure(0, weight=1)
        self.frame2.rowconfigure(1, weight=1)
        self.frame2.rowconfigure(2, weight=1)
        self.frame2.rowconfigure(3, weight=1)
        self.frame2.rowconfigure(4, weight=1)
        self.frame2.rowconfigure(5, weight=1)
        self.frame2.columnconfigure(4, weight=1)
        return self.frame2

