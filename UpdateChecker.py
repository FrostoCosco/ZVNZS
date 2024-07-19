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
