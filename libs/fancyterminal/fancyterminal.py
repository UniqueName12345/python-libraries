"""
FancyTerminal is a library for creating fancy terminal output.
"""

class FT_Terminal:
    def __init__(self):
        self.__version = '0.0.1'
    
    def error(self, message):
        """
        Prints an error message in red.
        """
        print('\033[91m' + message + '\033[0m')
    
    def error_input(self, message):
        """
        Makes an error message and returns the input.
        """
        return input('\033[91m' + message + '\033[0m')
    
    def success(self, message):
        """
        Prints a success message in green.
        """
        print('\033[92m' + message + '\033[0m')
    
    def success_input(self, message):
        """
        Makes a success message and returns the input.
        """
        return input('\033[92m' + message + '\033[0m')
    
    def warning(self, message):
        """
        Prints a warning message in yellow.
        """
        print('\033[93m' + message + '\033[0m')
    
    def warning_input(self, message):
        """
        Makes a warning message and returns the input.
        """
        return input('\033[93m' + message + '\033[0m')
    
    def info(self, message):
        """
        Prints an info message in blue.
        """
        print('\033[94m' + message + '\033[0m')
    
    def info_input(self, message):
        """
        Makes an info message and returns the input.
        """
        return input('\033[94m' + message + '\033[0m')
    
    def meta(self, message):
        """
        Prints a meta message in magenta.
        """
        print('\033[95m' + message + '\033[0m')
    
    def meta_input(self, message):
        """
        Makes a meta message and returns the input.
        """
        return input('\033[95m' + message + '\033[0m')
        
    def version(self):
        """
        Prints the version of the library.
        """
        self.meta('FancyTerminal v' + self.__version)