import os

path = input()

if os.path.exists(path):
    directory, filename = os.path.split(path)
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
else:
    print("The specified path does not exist.")

