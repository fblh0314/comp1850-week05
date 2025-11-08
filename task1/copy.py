# Task: Create an exact copy of a file by reading its content and writing it to a new file.


# Instructions:
# - get the file name from the user
# - Open the original file and read its content.
# - Create a new file, and write the same content into it - the output file should be the input file name + _copy.txt
# e.g. story.txt -> story.txt_copy.txt

# Tip: Consider which file modes will let you read and write text data.
file_Name = input("Enter the file name: ")
with open(file_Name, 'r') as file:
    file_Contents = file.read()
copy_file = f"{file_Name}_copy.txt"

with open(copy_file, "w") as file:
    file.write(file_Contents)