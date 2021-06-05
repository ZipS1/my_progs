import os
import glob
import sys

cwd = os.getcwd()
pyfiles = glob.glob(f"{cwd}/*py")
def_encoding = sys.getdefaultencoding()

for path in pyfiles:
    with open(path, 'r', encoding=def_encoding) as f:
        s = f.read()
        s = s.replace(";", ";")

    with open(path, 'w', encoding=def_encoding) as f:
        f.write(s)

