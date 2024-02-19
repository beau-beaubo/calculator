"""Sup Model"""
import tkinter as tk


class Keypad(tk.Frame):
    """Keypad"""
    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        # keynames and columns
        super().__init__(parent, **kwargs)
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        for i in range(len(self.keynames)):
            row = i // columns
            col = i % columns
            button = tk.Button(self, text=self.keynames[i])
            button.grid(row=row, column=col, sticky=tk.NSEW, padx=2, pady=2)

        for i in range(columns):
            self.columnconfigure(i, weight=1)
        for i in range(len(self.keynames) // columns):
            self.rowconfigure(i, weight=1)

    def bind(self, sequence=None, func=None, add=None):
        """Bind an event handler to an event sequence."""
        # as the bind method of Tkinter widgets.
        # Use the parameters to bind all the buttons in the keypad
        # to the same event handler.
        for button in self.winfo_children():
            button.bind(sequence, func, add)

    @property
    def frame(self):
        """get frame"""
        return self

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for button in self.winfo_children():
            button[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        for button in self.winfo_children():
            if key in button.keys():
                return button[key]
        return None

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        for button in self.winfo_children():
            # Configure each button with the provided keyword arguments
            button.configure(cnf, **kwargs)

    # the superclass object for this keypad.
    # This is so that a programmer can set properties of a keypad's frame,
    # e.g. keypad.frame.configure(background='blue')
