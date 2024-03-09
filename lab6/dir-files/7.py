with open('test.txt', 'r') as first, open('test2.txt', 'a') as second:
    for i in first:
        second.write(i)