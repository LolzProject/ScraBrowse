import os
os.system('pip install ScraGet')
# Built with ScraGet.
# Creds: https://github.com/Quantum-Codes/ScraGet
os.system('clear')
print("'info' for help.")

# NOTICE: "s!" stands for Search, it is the
# basic prefix for browser commands.

while True:
  option = input(">>> ")
  if option == "s!profile":
    profile = input("username>>> ")
    # Add code to retrieve data
