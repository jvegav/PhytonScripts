import os
file_path = '/Users/josuv/Downloads/ola.txt'

if os.path.isfile(file_path):
    os.remove(file_path)
    print("File hs successfully been Deleted")
else:
    print("This file does not exist")