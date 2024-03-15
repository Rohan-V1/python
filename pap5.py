import sys
file_name = input("Enter the file (or type 'exit' to stop): ")
if file_name.lower() == 'exit':
    print("Exiting the program.")
    sys.exit()
with open(file_name, 'w') as file:
    content = input("The contents are")
    while True:
        content = input()
        if content.lower() == 'exit':
            print("Exiting input. Contents saved to", file_name)
        break
    file.write(content + '\n')
with open(file_name, 'r') as file:
    words = 0
    chars = 0
    lines = 0
    for line in file:
        lines += 1
        list1 = line.split()
        words += len(list1)
        chars += len(line)-1
print("Lines:", lines)
print("Words:", words)
print("Characters:", chars)