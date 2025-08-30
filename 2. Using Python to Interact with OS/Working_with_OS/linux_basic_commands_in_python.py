import os
# Require Linux command tools or have to change the command in shell
# You can use Git Bash in the VSCode terminal to run the command 

# On Linux: ./ used to execute a file
# On Git Bash in VSCode: can't handle the command ./, instead call python
# Other command should work fine on both OS

# Run the python program to compare with the Linux command above
# echo $HOME
print("HOME: ", os.environ.get("HOME", "Not found"))       # "Not found": set fall back value
# echo $SHELL
print("SHELL: ", os.environ.get("SHELL", "Not found"))
# echo $PATH
print("PATH: ", os.environ.get("PATH", "Not found"))

# export GOAT=C.Ronaldo
os.environ["GOAT"] = "C.Ronaldo"
print("GOAT: ", os.environ.get("GOAT", "Not found"))

# cat linux_basic_commands_in_python.py
with open("linux_basic_commands_in_python.py", "r") as f:
    file = f.readlines()
    for line in file:
        print(line.strip())

# wc linux_basic_commands_in_python.py
line = 0
word = 0
char = 0
with open("linux_basic_commands_in_python.py", "rb") as f:
    file = f.read()
    line = file.count(b'\n')
    word = len(file.split())
    char = len(file)

print("Word count: ", line, word, char, "linux_basic_commands_in_python.py\n",end=" ")    

# echo $?
import subprocess

result = subprocess.run(["ls", "linux_basic_commands_in_python.py"])
print("Exit code:", result.returncode)



