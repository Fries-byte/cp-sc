# =--=--=--=--=--=--=--=--=--=--=--=--=
# PiStud's compiler source
# Created by PiStud-Lang (GitHub)
# and written by Fries-byte (GitHub)
# Learn more on our website or README.md
#
# 2025 - presents | The Programming Language PiStud
# =--=--=--=--=--=--=--=--=--=--=--=--=

import os
import sys
import urllib.request

def sc():
    if len(sys.argv) < 2:
        print("Usage: studc <filename>")
        sys.exit(1)

    fname = sys.argv[1]
    abs_path = os.path.abspath(fname)

    print(f"[DEBUG] Checking file at: {abs_path}")
    if not os.path.exists(abs_path):
        print("[ERROR] File does not exist! Check your path.")
        sys.exit(1)

    try:
        with open(abs_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"[ERROR] Failed to read file: {e}")
        sys.exit(1)
    modified_lines = []
    for line in lines:
        if "import package as ps" in line:
            modified_lines.append('exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/pistud/refs/heads/main/packages.py").read().decode())\n')
        else:
            modified_lines.append(line)

    try:
        with open(abs_path, "w", encoding="utf-8") as f:
            f.writelines(modified_lines)
    except Exception as e:
        print(f"[ERROR] Failed to write file: {e}")
        sys.exit(1)

    try:
        os.system(f"python -m pyinstaller --onefile {abs_path}")
    except Exception as e:
        print(f"[ERROR] Failed to run PyInstaller: {e}")
        sys.exit(1)

if __name__ == "__main__":
    sc()
