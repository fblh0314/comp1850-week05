# Task: Open a file and calculate the total number of lines, words, and characters.

# Instructions:
# - get the file name from the user
# - Read the file contents.
# - Count how many lines, words, and characters are in the file.
# - Print out the totals for each.
line_count = 0
char_count = 0
word_count = 0
file_Name = input("Enter the file name: ")

with open(file_Name, "r") as file:
    file_Contents = file.read()
    lines = file_Contents.splitlines()
    line_count = len(lines)

word_count = len(file_Contents.split())
char_count = len(file_Contents)

print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")
