# Read the file and store all lines in list
# Reverse the list
# Write the reversed list back to the file

with open('test.txt', 'r') as reader: # This line of code would open & close file in 'r' mode
    Contents = reader.readlines() # [apple, banana, cat, dog ,elephant]
    ReversedList = reversed(Contents) # [elephant, dog, cat, banana, apple]
    with open('test.txt', 'w') as writer: # This line of code would open & close file in 'w' mode
        for line in ReversedList:
            writer.write(line)


