# Writing to the file
file2 = open('output.txt', 'w')
user_input = input("Enter some data to write to the file: ")
file2.write(user_input + '\n')
file2.close()

# Appending to the same file
file2 = open('output.txt', 'a')
extra_input = input("Enter additional data to append: ")
file2.write(extra_input + '\n')
print('Data successfully written to output.txt')
file2.close()

# Reading and displaying final content
file2 = open('output.txt', 'r')
print("\nFinal content of the file:")
reading_line = file2.readline()
while reading_line:
    print(reading_line.strip())
    reading_line = file2.readline()
file2.close()

#output:
# Enter some data to write to the file: this is first input
# Enter additional data to append: This is append text
# Data successfully written to output.txt
#
# Final content of the file:
# this is first input
# This is append text

