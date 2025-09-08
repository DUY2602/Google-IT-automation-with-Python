import os
import subprocess

subprocess.run(["date"])         # Output current date
subprocess.run(["sleep", "2"])      # Pause the program for 2 seconds

result_1 = subprocess.run(["ls", "file_not_exist"])
print(result_1.returncode)          # Output: 2 (the error of listing not exist file)

# Sample code to check domain or IP address
result_2 = subprocess.run(["nslookup", "google.com"], capture_output=True)
print(result_2.returncode)
print(result_2.stdout)            # Output of the subprocess
print(result_2.stdout.decode().split())

# Sample code for removing the file that doesn't exist
result_3 = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result_3.returncode)          # Output: 1 (the error of removing not exist file)
print(result_3.stdout)
print(result_3.stderr)            # Because there's no result ouput, call stderr to see the error

import time

process = subprocess.Popen(['sleep', '5'])   # Create asynchronous (side process)
print("The process is running in the background...")
time.sleep(2)   # pause for 2 seconds  (the sub-process is still running)

while process.poll() is None:   # poll() to check if the sub-process is None (not finished) or int (finished)
    print("The process is still running.")
    time.sleep(1)

print("The process has finished.")