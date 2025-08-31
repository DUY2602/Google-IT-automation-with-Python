import sys

logfile = sys.argv[1]       # The file sample.log passed in at the end
with open(logfile) as f:
  for line in f:
    print(line.strip())
# When run on Git Bash: python log_file_with_python.py sample.log

print("\n\n\n")
# Example of using regular expression to search for a particular log event
logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    if "WARNING" not in line:         # Filter logs that contain WARNING
      continue
    print(line.strip())

print("\n\n\n")
# An example of using regular expression to analyze all waring logs for different usernames
import re
logfile = sys.argv[1]
usernames = {}          # Empty dictionary to store usernames 
with open(logfile) as f:
  for line in f:
    if "WARNING" not in line:
      continue
    pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (\w+) (\w+)"
    result = re.search(pattern, line)
    if result is not None:
      name = result[1]
      usernames[name] = usernames.get(name, 0) + 1

print(usernames)


