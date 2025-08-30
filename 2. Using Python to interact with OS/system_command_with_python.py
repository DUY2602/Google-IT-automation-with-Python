import subprocess

subprocess.run(["date"])
subprocess.run(["sleep", "2"])

result = subprocess.run(["ls", "file_not_exist"])
print(result.returncode)