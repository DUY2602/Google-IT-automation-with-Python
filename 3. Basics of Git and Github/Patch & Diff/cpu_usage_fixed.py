import psutil

def check_cpu_usage(percent):
    usage = psutil.cpu_percent(1)
    print("DEBUG: usage: {}".format(usage))
    return usage < percent

if not check_cpu_usage(75):
    print("ERROR! CPU is overloaded")
else:
    print("Everything ok")

# If you want to test, read this comment carefully:
# 1. Delete the cpu_usage.diff
# 2. Delete this comment
# 3. Run in Git Bash: diff -u cpu_usage.py cpu_usage_fixed.py > cpu_usage.diff
# to create a new .diff file store the differences
# 4. Run in Git Bash: patch cpu_usage.py < cpu_usage.diff