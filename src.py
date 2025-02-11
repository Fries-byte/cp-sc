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

def find_file(filename, search_path):
    """Recursively search for the file in the given directory."""
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

def sc():
    if len(sys.argv) < 2:
        print("Usage: studc <filename>")
        sys.exit(1)

    fname = sys.argv[1]  # Get the filename from the command line argument

    # Define search paths (e.g., current working directory, user's home directory)
    search_paths = [
        os.getcwd(),  # Current working directory
        os.path.expanduser("~"),  # User's home directory
    ]

    abs_path = None
    for path in search_paths:
        abs_path = find_file(fname, path)
        if abs_path:
            break

    if not abs_path:
        print(f"[ERROR] File '{fname}' not found in any of the search paths.")
        sys.exit(1)

    print(f"[DEBUG] Found file at: {abs_path}")

    try:
        with open(abs_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"[ERROR] Failed to read file: {e}")
        sys.exit(1)

    modified_lines = []
    for line in lines:
        if "import sys, os; sys.path.append(os.path.join(os.path.dirname(__file__), '..')); import package as ps" in line:
            modified_lines.append('import urllib.request;version=10;name="versions";exec(urllib.request.urlopen("https://raw.githubusercontent.com/Fries-byte/pistud/refs/heads/main/packages.py").read().decode());\n')
        else:
            modified_lines.append(line)

    try:
        with open(abs_path, "w", encoding="utf-8") as f:
            f.writelines(modified_lines)
    except Exception as e:
        print(f"[ERROR] Failed to write file: {e}")
        sys.exit(1)

    try:
        os.system(f"pyinstaller --onefile {abs_path}")
    except Exception as e:
        print(f"[ERROR] Failed to run PyInstaller: {e}")
        sys.exit(1)

if __name__ == "__main__":
    sc()
