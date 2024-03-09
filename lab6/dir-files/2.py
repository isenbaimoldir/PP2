import os

path = input("Enter a path: ")
if os.path.exists(path):
    dir_list = os.listdir(path)
    if dir_list:
        print(dir_list)
    else:
        print("empty")
        
    if os.access(path, os.R_OK):
        print(f"The path '{path}' is readable.")
    else:
        print(f"The path '{path}' is not readable.")

    if os.access(path, os.W_OK):
        print(f"The path '{path}' is writable.")
    else:
        print(f"The path '{path}' is not writable.")

    if os.access(path, os.X_OK):
        print(f"The path '{path}' is executable.")
    else:
        print(f"The path '{path}' is not executable.")
else:
    print("The specified path does not exist.")
