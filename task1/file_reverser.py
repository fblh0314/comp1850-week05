# Task: Reverse the text on each line of a file and save it to a new file.

# Instructions:
# - get the file name from the user
# - Open the original file and read each line.
# - Reverse the text of each line word by word -> 'hello my name is george' -> 'george is name my hello'
# - Write the reversed lines into a new file - the output file name should be the input filename + _reverse.txt
# for example: 'story.txt' -> 'story.txt_reverse.txt'
file_Name = input("Enter the file name: ")
with open(file_Name, 'r') as file:
    lines = [line.rstrip() + "\n" for line in file]
lines.reverse()
reverse_file = f"{file_Name}_reverse.txt"

with open(reverse_file, "w") as f:
    f.writelines(lines)
