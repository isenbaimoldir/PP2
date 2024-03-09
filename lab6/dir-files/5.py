lines = ["laskjd", "asdf", "asde", "werfr"]

with open('test.txt', 'w') as f:
    for line in lines:
        f.write(f"{line}\n")