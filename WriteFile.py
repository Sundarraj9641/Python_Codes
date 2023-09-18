# write() -- replace the content already present in the file
# close() the file after wrote the file
# place the text file and this python file in same location

file=open("FileHandling.txt","w")   # w -- write mode
file.write("Capgemini\n")
file.close()

# after closing the file you should open to read the updated file
file=open("FileHandling.txt","r")   # r -- read mode
content=file.read()
print(content)


# a -- append with already existing data, write() not replace the old content
file=open("FileHandling.txt","a")  # a -- append with already exixting
file.write("Sundarraj\n")
file.write("Software Engineer")
file.close()
file=open("FileHandling.txt","r")   # r -- read mode
c=file.read()

print(c)

# readLine() -- print a single line in the file













