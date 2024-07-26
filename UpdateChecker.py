# This file is used to automatically keep the game client up-to-date with newer releases of source ports and versions of ZVN.
# - @Divided

# Import libs.
import os
import platform

# Create a clear function.
def Clear():
  if platform.os == "Windows":
    os.system("cls")
  else:
    os.system("clear")

# Run some test code.
print("test!")

import gdown
import zipfile
import os

# URL of the file
url = 'https://drive.google.com/file/d/1KqLyaNZdOgjq0ZJ9-vFEl6I1clSkMfLS/view'

# Output file path
output = 'V3.zip'

# Download the file
gdown.download(url, output, quiet=False)
print(f'File downloaded and saved as {output}')

# Files and directories to exclude from extraction
excluded_paths = ["Savegames", "Screenshots"]

# Function to check if a file should be skipped
def should_skip(file_path):
    for excluded_path in excluded_paths:
        if file_path.startswith(excluded_path) or file_path == excluded_path:
            return True
    return False

# Extract the zip file, skipping the excluded files and directories
with zipfile.ZipFile(output, 'r') as zip_ref:
    for member in zip_ref.namelist():
        if not should_skip(member):
            zip_ref.extract(member, '.')

print('Extraction complete. Excluded files and directories have not been overwritten.')

# Delete the zip file
os.remove(output)
print(f'{output} has been deleted.')
