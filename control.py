"""Controller"""

from math import *
from playsound import playsound

class CalculatorControl:
    """Control"""
    def __init__(self):
        self.display = ""
        self.history = []

    def add_to_display(self, value):
        """Add value to the display."""
        self.display += value

    def clear_display(self):
        """Clear the display."""
        self.display = ""

    def delete_last_char(self):
        """Delete the last character from the display."""
        if self.display:
            self.display = self.display[:-1]
        for math_func in ['sqrt', 'log', 'log10', 'log2', 'exp']:
            if self.display.endswith(math_func):
                func = math_func
                self.display = self.display.replace(func, '')

    def evaluate_display(self):
        """Evaluate the expression in the display."""
        try:
            result = eval(self.display)
            self.display = str(result)
            return result
        except Exception as e:
            return str(e)

    def get_display(self):
        """Return the current display value."""
        return self.display

    def is_valid_expression(self):
        """Check if the current display value forms a valid expression."""
        try:
            eval(self.display)
            return True
        except:
            return False

    def raise_error(self):
        """error"""
        if self.is_valid_expression() is False:
            playsound('error.mp3', False)


    def add_to_history(self, expression, result):
        """Add an expression and its result to the history."""
        history_text = f"{expression} = {result}"
        self.history.append(history_text)

    def get_history(self):
        """Return the history."""
        return self.history if hasattr(self, 'history') else []
