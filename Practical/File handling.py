# TASK: Use a text editor to create a file
# called info.txt and enter the text shown below.
# Once the file has been created and saved, write
# a small program that:
file = open("info.txt")
print(file.read())
file.close()

# TASK: write a small program that opens the
# info.txt file, then reads and displays each
# of the three lines of text using calls to the
# readline() method. Remember to close the file
# once the content has been read.
file = open("info.txt")
myline = file.readline()
while myline:
    print(myline)
    myline = file.readline()

file.close()

# TASK: Write a small program that opens the
# "info.txt" file in append (a) mode. Use the write()
# method to add an extra line of text saying
# "this is an extra line". Remember to close the
# file once the content has been read. Open the file
# with a text editor and examine the contents.

file = open("info.txt", "a")
file.write("This is written to the file")
file.close()

# TASK: write a small program that opens the info.txt
# file, then reads and displays each line of text
# using a for...in loop. Rather than explicitly call
# the close() method, use the ‘with’ statement to wrap
# the file handling code.


with open("info.txt", "r") as f:
    for line in f:
        print(line)
