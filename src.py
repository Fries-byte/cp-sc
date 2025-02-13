# =--=--=--=--=--=--=--=--=--=--=--=--=
# PiStud's compiler source
# Created by PiStud-Lang (GitHub)
# and written by Fries-byte (GitHub)
# Learn more on our website or README.md
#
# 2025 - presents | The Programming Language PiStud
# =--=--=--=--=--=--=--=--=--=--=--=--=

import os
import urllib.request
import subprocess
import sys

def modify_file(file_path, url):
    try:
        with urllib.request.urlopen(url) as response:
            new_content = response.read().decode('utf-8')

        with open(file_path, 'r') as file:
            original_lines = file.readlines()

        original_lines[0] = new_content + '\n'

        with open(file_path, 'w') as file:
            file.writelines(original_lines)

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def revert_file(file_path, original_lines):
    with open(file_path, 'w') as file:
        file.writelines(original_lines)

def compile_with_pyinstaller(file_path):
    print(f"Compiling {file_path} with PyInstaller...")
    try:
        subprocess.run([sys.executable, '-m', 'PyInstaller', '--onefile', file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during compilation: {e}")
    except FileNotFoundError as e:
        print(f"PyInstaller not found. Ensure it is installed and in the PATH: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python src.py <target_file>")
        return

    target_file = sys.argv[1]
    url = "https://raw.githubusercontent.com/Fries-byte/pistud/refs/heads/main/src/ps.py"

    with open(target_file, 'r') as file:
        original_lines = file.readlines()

    if not modify_file(target_file, url):
        return

    compile_with_pyinstaller(target_file)

    revert_file(target_file, original_lines)

if __name__ == "__main__":
    main()
