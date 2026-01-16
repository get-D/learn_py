# Use the shutil module to: 
# Copy a file from one folder to another
# Move a file to a new folder
# Delete a file (careful: irreversible!)


import shutil
import os


shutil.copy("task.txt", "my_folder/task.txt")
shutil.move("task.txt", "my_folder/task.txt")
os.remove("my_folder/task.txt")