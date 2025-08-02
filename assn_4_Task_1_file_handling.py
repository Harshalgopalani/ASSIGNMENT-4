
try:
    file1 = open('sample6.txt', 'r+')
    reading_file = file1.readline()

    while reading_file:
        print(reading_file.strip())
        reading_file = file1.readline()

    file1.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

#output:
# This is sample text file
# It contains multiple lines!

#If file not found output will be :
# Error: The file 'sample.txt' does not exist.






# file1 = open('my_file.txt', 'r+')
# writing_file = file1.read()
# print(writing_file)
# file1.close()
#
# my_dict = {'key1':1, 'key2':9, 'key3':[333], 'key4':6, 'key5':[444]}
# print(my_dict['key4'])

