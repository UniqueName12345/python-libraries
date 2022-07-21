import filemanagement

f = filemanagement.FileManager('\\tmp', 'test.txt')
f.create_file()
f.open_file()