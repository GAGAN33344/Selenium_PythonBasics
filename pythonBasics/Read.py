# Read one sigle line at a time, don't mix read & readline methods
file = open('test.txt')

# print(file.read()) # It would read all contents of file

# print(file.read(5)) # It would read content based on Index parameters

# print(file.readline()) # It would read whole line
# print(file.readline()) # It would read whole line

# file.close()

# Print line by line using readline method
#line = file.readline()
#while line!="":
#    print(line)
#    line = file.readline()

for i in file.readlines():
    print(i)


file.close()



