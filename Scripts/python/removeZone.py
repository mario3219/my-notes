#!/usr/bin/env python3
"""
Usage:
    * Ensure script is executable:
        chmod +x removeZone.py
    * Run from terminal:
        python3 removeZone.py <folder adress> <substring>
"""
import os
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python remove_files.py <folder_path> <substring>")
        sys.exit(1)

    folder = sys.argv[1]
    substring = sys.argv[2]

    # Check that folder exists
    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a directory.")
        sys.exit(1)

    # Loop through files
    removed_count = 0
    for filename in os.listdir(folder):
        if substring in filename:
            filepath = os.path.join(folder, filename)
            if os.path.isfile(filepath):
                print(f"Removing: {filepath}")
                os.remove(filepath)
                removed_count += 1

    print(f"Done. Removed {removed_count} files.")

if __name__ == "__main__":
    main()
