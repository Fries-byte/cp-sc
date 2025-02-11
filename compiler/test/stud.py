import os
import sys
import urllib.request

def find_file(filename, search_path):
    """Recursively search for the file in the given directory."""
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

def fetch_content(url):
    """Fetch content from the given URL."""
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        print(f"[ERROR] Failed to fetch content from {url}: {e}")
        sys.exit(1)

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

    # Read the original content of the file
    try:
        with open(abs_path, "r", encoding="utf-8") as f:
            original_lines = f.readlines()
    except Exception as e:
        print(f"[ERROR] Failed to read file: {e}")
        sys.exit(1)

    # Fetch the replacement content from the URL
    replacement_content = fetch_content("https://raw.githubusercontent.com/Fries-byte/pistud/refs/heads/main/src/ps.py")

    # Modify the file
    modified_lines = []
    for line in original_lines:
        print(f"[DEBUG] Processing line: {line.strip()}")  # Debug print
        if "import sys, os; sys.path.append(os.path.join(os.path.dirname(__file__), '..')); import package as ps" in line:
            print("[DEBUG] Found target line, replacing it.")  # Debug print
            # Replace the target line with the fetched content
            modified_lines.append(replacement_content + "\n")
        else:
            modified_lines.append(line)

    try:
        with open(abs_path, "w", encoding="utf-8") as f:
            f.writelines(modified_lines)
    except Exception as e:
        print(f"[ERROR] Failed to write file: {e}")
        sys.exit(1)

    # Compile the file using PyInstaller
    try:
        os.system(f"pyinstaller --onefile {abs_path}")
    except Exception as e:
        print(f"[ERROR] Failed to run PyInstaller: {e}")
        # Restore the original content in case of failure
        try:
            with open(abs_path, "w", encoding="utf-8") as f:
                f.writelines(original_lines)
        except Exception as restore_error:
            print(f"[ERROR] Failed to restore original file: {restore_error}")
        sys.exit(1)

    # Restore the original content after successful compilation
    try:
        with open(abs_path, "w", encoding="utf-8") as f:
            f.writelines(original_lines)
        print("[DEBUG] Original file content restored.")
    except Exception as e:
        print(f"[ERROR] Failed to restore original file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    sc()
