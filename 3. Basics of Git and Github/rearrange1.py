import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])

# diff rearrange1.py rearrange2.py
# Output:
# 4c4
# <     result = re.search(r"^([\w .]*), ([\w .]*)$", name)
# ---
# >     result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)