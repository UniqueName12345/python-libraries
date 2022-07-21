"""
Easy file management using the OS's file system.
"""
import os

class FileManager:

    """
    This is what you call when you need to do stuff related to files
    """

    def __init__(self, path, name):
        self.path = path
        self.name = name
    
    def create_file(self):
        """
        Create a file in the given path
        """
        try:
            with open(os.path.join(self.path, self.name), 'w') as f:
                f.write('')
        except Exception as e:
            print(e)
    
    def open_file(self):
        """
        Open a file in the given path
        """
        try:
            with open(os.path.join(self.path, self.name), 'r') as f:
                print(f.read())
        except Exception as e:
            print(e)
        
    def write_file(self, content):
        """
        Write content to a file in the given path
        """
        try:
            with open(os.path.join(self.path, self.name), 'w') as f:
                f.write(content)
        except Exception as e:
            print(e)