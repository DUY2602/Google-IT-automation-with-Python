import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    print(line.strip())
