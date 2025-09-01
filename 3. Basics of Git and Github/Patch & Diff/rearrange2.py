import re

def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])

# diff -u rearrange1.py rearrange2.py
# Output:

"""
--- rearrange1.py       2025-09-01 05:01:57.931020500 +0700
+++ rearrange2.py       2025-09-01 05:07:32.182613400 +0700
@@ -1,9 +1,9 @@       # 2 files' length (9 lines)
 import re

 def rearrange_name(name):
-    result = re.search(r"^([\w .]*), ([\w .]*)$", name)       # The difference between
+    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)     # 2 files + & -
     if result == None:
         return name
     return "{} {}".format(result[2], result[1])

\ No newline at end of file
"""