"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

with open('foo.txt') as file:
    read_data = file.read()
    print(read_data)

file.closed
# with key words closes file autimaticly
# but it's important to make sure the file is alctualy closed.

print("--------------")

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open('bar.txt', 'w') as file:
    file.write('Text in line 1. \nText in line 2. \nText in line 3.')

with open('bar.txt') as file:
    file_data = file.read()
    print(file_data)
