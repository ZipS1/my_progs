import os
import glob

cwd = os.getcwd()
pyfiles = glob.glob(f"{cwd}/*py")
tags = ("corona", "ucorona", "uucorona")

for path in pyfiles:
    with open(path, 'r') as f:
        lines = f.readlines()

    for tag in tags:
        open_tag = f"# {tag}0\n"
        close_tag = f"# {tag}\n"
        while open_tag in lines:
            ind = lines.index(open_tag)
            while lines[ind] != close_tag:
                lines.pop(ind)
            lines.pop(ind)

    with open(path, 'w') as f:
        f.writelines(lines)

