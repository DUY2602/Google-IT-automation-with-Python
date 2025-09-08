import re

def count_log(log):
    regex = rf"{log}"
    with open ("sample.log", "r") as f:
        for line in f:
            target = re.search(regex, line)
            if target:
                print(line)

count_log("ERROR")