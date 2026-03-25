with open("newfile.txt", "w") as file:
    file.write('''Hello new 1st line.
Second line.
third line''')
    file.close()

with open("newfile.txt", "r") as file:
    data = file.read()
    print(data)

    file.seek(0)
# give only 1st line of the file
    reads = file.readline()
    print(reads)
    
    file.seek(0)
# give the whole file into list
    readls = file.readlines()
    print(readls)

    line1 = len(readls)
    word = 0
    for line in data:
        words = data.split()
        word = len(words)
    print("No. of words:", word)
    print("No. of lines:", line1)