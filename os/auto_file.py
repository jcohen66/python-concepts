# Automate File Management

import os
import shutil
import glob

# Move files
def move_files(source, dest):
    for file in glob.glob(source):
        shutil.move(file, dest)
        

# Copy Files
def copy_files(source, dest):
    for file in glob.glob(source):
        shutil.copy(file, dest)
        
        
# Delete Files
def delete_files(source):
    for file in glob.glob(source):
        os.remove(file)
        
        
# Rename Files
def rename_files(source, dest):
    for file in glob.glob(source):
        os.mkdir(folder)
        
        
# Create Folders
def create_folders(source):
    for folder in glob.glob(source):
        os.mkdir(folder)
        
# Delete Folders
def delete_folders(source):
    for folder in glob.glob(source):
        os.rmdir(folder)
        
        
# Rename Folders
def rename_folders(source, dest):
    for folder in glob.glob(source):
        os.rename(folder, dest)
        
        
# Search File
def search_file(source, search):
    for file in glob.glob(source):
        if search in file:
            print(file)
            

# List Files in Directory
def list_files(source):
    for file in glob.glob(source):
        print(file)