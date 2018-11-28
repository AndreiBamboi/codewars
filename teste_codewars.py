infile = open(r"./Client_script/file.txt", "r")
line = infile.readline()
while line:
    values = line.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[2] )
    line = infile.readline()

infile.close()