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

home_dir = os.path.expanduser("~")
script_dir = os.path.join(home_dir, "scripts")
script_path = os.path.join(script_dir, "studc.py")
powershell_profile = os.path.join(home_dir, "Documents", "WindowsPowerShell", "Microsoft.PowerShell_profile.ps1")
os.makedirs(script_dir, exist_ok=True)
studc_script_content = '''import subprocess
import sys

def sc():
    if len(sys.argv) < 2:
        print("Usage: studc <filename>")
        sys.exit(1)

    fname = sys.argv[1]  # Get the filename from command-line arguments
    subprocess.run(f"pyinstaller --onefile {fname}", shell=True)

if __name__ == "__main__":
    sc()
'''
with open(script_path, "w", encoding="utf-8") as file:
    file.write(studc_script_content)

print(f"[✔] Created 'studc.py' at {script_path}")

alias_command = f'function studc {{ python "{script_path}" $args }}\n'

if not os.path.exists(powershell_profile):
    open(powershell_profile, "w").close()

with open(powershell_profile, "r+", encoding="utf-8") as file:
    content = file.read()
    if alias_command not in content:
        file.write("\n" + alias_command)
        print("[✔] Added 'studc' alias to PowerShell profile.")
    else:
        print("[!] 'studc' alias already exists in PowerShell profile.")

print("\n[⚠] Please restart your PowerShell or run the following command to reload the profile:\n")
print(f"    . {powershell_profile}")
