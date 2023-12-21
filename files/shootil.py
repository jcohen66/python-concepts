import shutil

x = shutil.copy("first.txt","second.txt")

x = shutil.copytree("sourcedir", "targetdir")
print(x)

def ignore_specific_files(directory, files):
    return [f for f in files if f == 'file1.txt']

shutil.copytree("sourcedir", "targetdir2")
