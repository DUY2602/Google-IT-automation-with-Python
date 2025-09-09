import re

def count_log():
    log = input("What logging status do you want to check: (ERROR, INFO, WARNING) ")
    regex = rf"{log}"
    with open ("sample.log", "r") as f:
        count = 0
        for line in f:
            target = re.search(regex, line)
            if target:
                print(line)
                count += 1
    print(f"There are {count} ERROR occur")

# count_log("ERROR")

def get_date_status():
    date = input("What date do you want to check:  (YYYY-MM-DD) ")
    print(f"Listing the logging status for day: {date}")
    regex = rf"{date}"
    with open ("sample.log", "r") as f:
        for line in f:
            target = re.search(regex, line)
            if target:
                print(line)

get_date_status()