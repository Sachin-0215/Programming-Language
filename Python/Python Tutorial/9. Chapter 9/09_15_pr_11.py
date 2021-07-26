# WAP program to rename a file to "renamed_by_python.txt"

import os

oldname = "renamed_by_python.txt"
newname = "log.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)